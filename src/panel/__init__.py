import numpy as np
from pandas import DataFrame as DataFrame


def schmitt_trigger(val: np.ndarray, on: float, off: float, init: int = 0) -> np.ndarray:
    val = np.asarray(val)

    up = val >= on
    down = val <= off
    t = np.arange(val.shape[-1])

    on_t  = np.where(up, t, -1)
    off_t = np.where(down, t, -1)

    last_on  = np.maximum.accumulate(on_t)
    last_off = np.maximum.accumulate(off_t)

    y = last_on > last_off

    no_event_yet = (last_on == -1) & (last_off == -1)
    if init:
        y = y | no_event_yet

    return y.astype(np.int8)


def debounce_binary_after_schmitt(bins, n_frames: int):
    x = bins
    if x.size == 0:
        return np.array([], dtype=np.uint8)
    if n_frames is None or n_frames <= 1:
        return x.copy()

    n = int(n_frames)
    y = x.copy()

    state = int(x[0])
    y[0] = state

    pending = None   # candidate new state (0/1) waiting to be confirmed
    cnt = 0          # how many consecutive frames we've seen for pending

    for i in range(1, x.size):
        v = int(x[i])

        if v == state:
            # stable, cancel any pending transition
            pending = None
            cnt = 0
            y[i] = state
            continue

        # v != state: possible transition
        if pending is None or pending != v:
            pending = v
            cnt = 1
        else:
            cnt += 1

        if cnt >= n:
            # confirm transition; backfill so the change happens at the first
            # frame of the stable run (not delayed by n-1 frames)
            state = pending
            start = i - n + 1
            y[start:i+1] = state
            pending = None
            cnt = 0

        y[i] = state

    return y
