# Code Kata----Leap Years
# Write a function that returns true or false depending on whether its
# input integer is a leap year or not. A leap year is divisible by 4, but is not 
# otherwise divisible by 100, unless it is also divisible by 400.
# Examples:
# 1996 ---> true
# 2001 ---> false
# 2000 ---> true
# 1900 ---> false



def is_leap(year):
    return is_typical_leap_year(year) and not is_atypical_common_year(year)
    
def is_typical_leap_year(year):
    return year % 4 ==0
def is_atypical_common_year(year):
      return year % 100 == 0 and not year % 400 == 0
      
def test_normal_leap_year():
    assert is_leap(1996)
    
def test_normal_common_year():
     assert not is_leap(2001)
     
def test_atypical_common_year():
     assert not is_leap(1900)

def test_atypical_leap_year():
     assert is_leap(2000)