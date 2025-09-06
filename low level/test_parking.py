
# We need to import the function we want to test
from test import calculate_fee 

def test_non_ntu_under_30_min():
    """
    Tests the case for a non-NTU member parking for less than 30 minutes.
    Expected fee: 20
    """
    assert calculate_fee("10:00", "10:29", is_ntu=False) == 20
