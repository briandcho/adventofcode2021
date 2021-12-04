def count_increases(sweep_data: list[int]) -> int:
    n_increases = 0
    for i in range(1, len(sweep_data)):
        if sweep_data[i - 1] < sweep_data[i]:
            n_increases += 1
    return n_increases


def count_window_increases(sweep_data: list[int]) -> int:
    n_increases = 0
    for i in range(1, len(sweep_data)):
        last_window = sweep_data[i - 1 : i + 2]
        window = sweep_data[i : i + 3]
        if sum(last_window) < sum(window):
            n_increases += 1
    return n_increases
