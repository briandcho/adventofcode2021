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


def navigate_no_aim(planned_course: list[str]) -> int:
    h_pos = depth = 0
    for cmd in planned_course:
        dir_, n = cmd.split()
        if dir_ == "forward":
            h_pos += int(n)
        elif dir_ == "down":
            depth += int(n)
        else:
            depth -= int(n)
    return h_pos * depth


def navigate(planned_course: list[str]) -> int:
    aim = h_pos = depth = 0
    for cmd in planned_course:
        dir_, n = cmd.split()
        if dir_ == "forward":
            h_pos += int(n)
            depth += int(n) * aim
        elif dir_ == "down":
            aim += int(n)
        else:
            aim -= int(n)
    return h_pos * depth
