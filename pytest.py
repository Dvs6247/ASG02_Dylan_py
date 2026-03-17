def test_something():
    # 1. ARRANGEE - set up the objects you need
    m = Manufacturer("Honda", "Japan")

    # 2. ACT - call the method you are testing
    result = str(m)

    # 3. ASSERT - check that the result is what you expected
    assert result == "Honda, Japan"

def test_will_fail():
    assert 1 + 1 == 3
