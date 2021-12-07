from typing import Callable


def count_increases(sweep_data: list[int]) -> int:
    return sum(sweep_data[i - 1] < sweep_data[i] for i in range(1, len(sweep_data)))


def count_window_increases(sweep_data: list[int]) -> int:
    return sum(sweep_data[i - 3] < sweep_data[i] for i in range(3, len(sweep_data)))


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


def get_power_consumption(diagnostic_report: list[str]) -> int:
    gamma = epsilon = ""
    n_rows = len(diagnostic_report)
    for pos in range(len(diagnostic_report[0])):
        n_bits = sum(int(row[pos]) for row in diagnostic_report)
        gamma += str(int(n_bits > n_rows - n_bits))
        epsilon += str(int(n_bits <= n_rows - n_bits))
    return int(gamma, 2) * int(epsilon, 2)


def get_life_support_rating(diagnostic_report: list[str]) -> int:
    oxygen_generator_rating = rating_for_bit_criteria(
        diagnostic_report,
        lambda m, n: m >= n - m,
    )
    co2_scrubber_rating = rating_for_bit_criteria(
        diagnostic_report,
        lambda m, n: m < n - m,
    )
    return oxygen_generator_rating * co2_scrubber_rating


def rating_for_bit_criteria(
    rows: list[str],
    criteria: Callable[[int, int], bool],
) -> int:
    for pos in range(len(rows[0])):
        if len(rows) == 1:
            break
        n_bits = sum(int(row[pos]) for row in rows)
        bit_value = str(int(criteria(n_bits, len(rows))))
        rows = [row for row in rows if row[pos] == bit_value]
    return int(rows[0], 2)
