from typing import Callable


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


def get_power_consumption(diagnostic_report: list[str]) -> int:
    n_bits = len(diagnostic_report[0])
    gamma = epsilon = ""
    for pos in range(n_bits):
        n_ones = n_zeroes = 0
        for row in diagnostic_report:
            if row[pos] == "1":
                n_ones += 1
            else:
                n_zeroes += 1
        gamma += str(int(n_ones > n_zeroes))
        epsilon += str(int(n_ones <= n_zeroes))
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
