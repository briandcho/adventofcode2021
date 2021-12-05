import pytest

import testing


@pytest.fixture
def day1_sweep_report():
    return list(testing.SWEEP_REPORT)
