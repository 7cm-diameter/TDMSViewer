import numpy as np
import pandas as pd

MAX_SAMPLES = 20_000


class TimeData:
    def __init__(self, name: str, df: pd.DataFrame, max_samples: int = MAX_SAMPLES):
        self.name = name
        self.df = df
        self.N = len(df)
        self.max_points = int(max_samples)

    def _make_indices(self, start: int, end: int) -> np.ndarray:
        n = end - start
        m = self.max_points

        if m <= 0 or n <= 0:
            return np.empty((0,), dtype=np.int64)

        if n <= m:
            return np.arange(start, end, dtype=np.int64)

        return np.linspace(start, end - 1, num=m, dtype=np.int64)

    def get_chunk(
        self,
        cols: list[str],
        start: int,
        window: int,
        dtype=np.float32,
    ) -> tuple[np.ndarray, dict[str, np.ndarray]]:
        N = self.N
        start = int(start)
        window = int(window)
        if window < 0:
            window = 0

        start = max(0, min(start, N))
        end = max(start, min(start + window, N))

        idx = self._make_indices(start, end)

        out: dict[str, np.ndarray] = {}
        for c in cols:
            if c not in self.df.columns:
                out[c] = np.empty((0,), dtype=dtype)
                continue

            a = self.df[c].to_numpy()
            out[c] = a[idx].astype(dtype, copy=False)

        return idx, out
    
    def get_col(self, col, dtype=np.float32):
        return self.df[col].to_numpy(dtype, copy=False)

class DataSource:
    def __init__(self, td: TimeData, name: str = "main"):
        self._sources: dict[str, TimeData] = {name: td}
        self.N = td.N

    @property
    def sources(self) -> list[str]:
        return list(self._sources.keys())

    @property
    def columns(self, src: str) -> list[tuple[str, str]]:
        td = self._sources[src]
        return [(src, str(c)) for c in td.df.columns]

    def get_chunk_from_source(
        self,
        src: str | None,
        cols: list[str],
        start: int,
        window: int,
    ) -> tuple[np.ndarray, dict[str, np.ndarray]]:
        return self._sources[src].get_chunk(cols, start, window)

    def set_source(self, src: str, df: pd.DataFrame):
        if src in self._sources:
            raise ValueError(f"{src}はすでにデータソース内に存在します")
        if self.N != len(df):
            raise ValueError("新しいデータフレームと既存のデータフレームの長さは同じでなければならない")
        self._sources[src] = TimeData(src, df)

    def get_source_col(self, source: str, col: str):
        return self._sources[source].get_col(col)
