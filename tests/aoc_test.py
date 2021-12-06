import pytest

import aoc
from testing import DAY1_SWEEP_REPORT
from testing import DAY2_PLANNED_COURSE
from testing import DAY3_DIAGNOSTIC_REPORT

# Day 1


@pytest.mark.parametrize(
    ("sweep_report", "n_increases"),
    (
        ((0,), 0),
        ((0, 0), 0),
        ((0, 1), 1),
        ((0, 1, 2), 2),
        ((199, 200, 208, 210, 200, 207, 240, 269, 260, 263), 7),
        (DAY1_SWEEP_REPORT, 1233),
    ),
)
def test_count_increases(sweep_report, n_increases):
    assert aoc.count_increases(sweep_report) == n_increases


@pytest.mark.parametrize(
    ("sweep_report", "n_increases"),
    (
        ((0,), 0),
        ((0, 0), 0),
        ((0, 1), 0),
        ((0, 1, 2), 0),
        ((0, 1, 2, 3), 1),
        ((199, 200, 208, 210, 200, 207, 240, 269, 260, 263), 5),
        (DAY1_SWEEP_REPORT, 1275),
    ),
)
def test_count_window_increases(sweep_report, n_increases):
    assert aoc.count_window_increases(sweep_report) == n_increases


# Day 2


@pytest.mark.parametrize(
    ("planned_course", "position"),
    (
        (("forward 1",), 0),
        (("forward 1", "down 1"), 1),
        (("forward 1", "down 2", "up 1"), 1),
        (
            (
                "forward 5",
                "down 5",
                "forward 8",
                "up 3",
                "down 8",
                "forward 2",
            ),
            150,
        ),
        (DAY2_PLANNED_COURSE, 2019945),
    ),
)
def test_navigate_no_aim(planned_course, position):
    assert aoc.navigate_no_aim(planned_course) == position


@pytest.mark.parametrize(
    ("planned_course", "position"),
    (
        (("forward 1",), 0),
        (("forward 5", "down 5"), 0),
        (("forward 5", "down 5", "forward 8"), 520),
        (("forward 5", "down 5", "forward 8", "up 3"), 520),
        (("forward 5", "down 5", "forward 8", "up 3", "down 8"), 520),
        (("forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"), 900),
        (DAY2_PLANNED_COURSE, 1599311480),
    ),
)
def test_navigate(planned_course, position):
    assert aoc.navigate(planned_course) == position


# Day 3


@pytest.mark.parametrize(
    ("diagnostic_report", "consumption"),
    (
        (("00100",), 108),
        (("00100", "11110", "10110"), 198),
        (
            (
                "00100",
                "11110",
                "10110",
                "10111",
                "10101",
                "01111",
                "00111",
                "11100",
                "10000",
                "11001",
                "00010",
                "01010",
            ),
            198,
        ),
        (DAY3_DIAGNOSTIC_REPORT, 3969000),
    ),
)
def test_get_power_consumption(diagnostic_report, consumption):
    assert aoc.get_power_consumption(diagnostic_report) == consumption
