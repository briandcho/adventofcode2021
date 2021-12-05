import pytest

import aoc
from testing import DAY1_SWEEP_REPORT
from testing import DAY2_PLANNED_COURSE


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
def test_navigate(planned_course, position):
    assert aoc.navigate(planned_course) == position
