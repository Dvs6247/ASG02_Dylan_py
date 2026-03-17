def test_something():
    # 1. ARRANGEE - set up the objects you need
    m = Manufacturer("Honda", "Japan")

    # 2. ACT - call the method you are testing
    result = str(m)

    # 3. ASSERT - check that the result is what you expected
    assert result == "Honda, Japan"

def test_will_fail():
    assert 1 + 1 == 3

class TestManufacturer:

    # Creating the full test class for Manufacturer

    def test_constructor_and_getters(self):
        m = Manufacturer("Ford", "USA")
        assert m.name == "Ford"
        assert m.country == "USA"

    def test_str(self):
        m = Manufacturer("Honda", "Japan")
        assert str(m) == "Honda, Japan"

    def test_different_manufacturer(self):
        m = Manufacturer("BMW", "Germany")
        assert m.name == "BMW"
        assert m.country == "Germany"
        assert str(m) == "BMW, Germany"

class TestAutoModel:
    #Creating the full test class for AutoModel.
    def test_constructor_and_getters(self):
        am = AutoModel("Civic", False, [1996, 1997, 1998])
        assert am.name == "Civic"
        assert am.in_production is False
        assert am.years == [1996, 1997, 1998]

    def test_first_year(self):
        am = AutoModel("F150", True, [2020, 2021, 2022])
        assert am.first_year == 2020

    def test_str(self):
        am = AutoModel("M3 Limited", False, [2015, 2016, 2017, 2018])
        result = str(am)
        assert "M3 Limited" in result
        assert "False" in result
        assert "2015" in result

    def test_empty_years_raises(self):
        with pytest.raises(ValueError):
            AutoModel("Ghost", False, [])

    def test_years_defensive_copy(self):
        """Mutating the original list must NOT affect the mods"""
        original = [2000, 2001]
        am = AutoModel("Test", True, original)
        original.append(2002)
        assert len(am.years) == 2

    def test_year_getter_returns_copy(self):
        """Mutating the returned list must NOT affect the mods"""
        am = AutoModel("Test", True, [2000, 2001])
        returned = am.years
        returned.append(2002)
        assert len(am.years) == 2

        