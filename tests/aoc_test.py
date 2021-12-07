import pytest

import aoc
from testing import DAY1_SWEEP_REPORT
from testing import DAY2_PLANNED_COURSE
from testing import DAY3_DIAGNOSTIC_REPORT
from testing import DAY4_BOARDS
from testing import DAY4_DRAWS

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


@pytest.mark.parametrize(
    ("diagnostic_report", "life_support_rating"),
    (
        (("10111",), 529),
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
            230,
        ),
        (DAY3_DIAGNOSTIC_REPORT, 4267809),
    ),
)
def test_get_life_support_rating(
    diagnostic_report,
    life_support_rating,
):
    assert aoc.get_life_support_rating(diagnostic_report) == life_support_rating


@pytest.mark.parametrize(
    ("draws", "boards", "score"),
    (
        (
            "7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1",
            [
                "22 13 17 11  0\n"
                " 8  2 23  4 24\n"
                "21  9 14 16  7\n"
                " 6 10  3 18  5\n"
                " 1 12 20 15 19",
                " 3 15  0  2 22\n"
                " 9 18 13 17  5\n"
                "19  8  7 25 23\n"
                "20 11 10 24  4\n"
                "14 21 16 12  6",
                "14 21 17 24  4\n"
                "10 16 15  9 19\n"
                "18  8 23 26 20\n"
                "22 11 13  6  5\n"
                " 2  0 12  3  7",
            ],
            4512,
        ),
        (DAY4_DRAWS, DAY4_BOARDS, 5685),
    ),
)
def test_bingo(draws, boards, score):
    assert aoc.bingo(boards, draws) == score
