import pytest

import testing


@pytest.fixture
def day1_sweep_report():
    return list(testing.SWEEP_REPORT)


@pytest.fixture
def day2_planned_course():
    return list(testing.PLANNED_COURSE)
