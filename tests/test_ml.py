import ml

def test_median():
    assert ml.func1() == 86.5

def test_percentage():
    assert ml.func2() < 50

def test_addition():
    assert ml.add(4,5) == 9
    assert ml.add(5, 6) == 12
    assert ml.add(4, 5) == 9

def test_division():
    assert ml.product(4) == 8
    
