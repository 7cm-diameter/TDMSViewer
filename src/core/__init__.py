def make_dummy_df(N=200_000, fs=1000):
    import numpy as np
    from pandas import DataFrame
    t = np.arange(N, dtype=np.float32) / fs
    df = DataFrame(
        {
            "sin_3hz": np.sin(2 * np.pi * 3 * t).astype(np.float32),
            "sin_4hz": (1.5 * np.sin(2 * np.pi * 4 * t)).astype(np.float32),
            "sin_6hz": (1.0 * np.sin(2 * np.pi * 6 * t)).astype(np.float32),
            "sin_9hz": (0.5 * np.sin(2 * np.pi * 9 * t)).astype(np.float32),
            "noise": (0.15 * np.random.randn(N)).astype(np.float32),
        }
    )
    return df
