def is_leap(year):
    return True

def test_normal_leap_year():
    assert is_leap(1996)
def test_normal_common_year():
     assert not is_leap(2001)
