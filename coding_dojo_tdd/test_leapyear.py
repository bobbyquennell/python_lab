def is_leap(year):
    return year % 4 == 0

def test_normal_leap_year():
    assert is_leap(1996)
def test_normal_common_year():
     assert not is_leap(2001)
     
def test_atypical_common_year():
     assert not is_leap(1900)
