from interest import simple_interest

def test_interest_1():
    assert simple_interest(1000, 5, 2) == 100

def test_interest_2():
    assert simple_interest(2000, 10, 3) == 600

def test_interest_3():
    assert simple_interest(5000, 4, 2) == 400