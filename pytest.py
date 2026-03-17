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

class TestVehicleAbstract:
    #Created the full test class for the VehicleAbstract
    def test_vehicle_cannot_be_instantiated(self):
        '''Vehicle is abstract and should not be directly instantiated'''
        with pytest.raises(TypeError):
            Vehicle(
                Manufacturer("X", "Y"),
                AutoModel("Z", True, [2020]),
                25.0,
            )

    def test_subclass_must_implement_number_of_wheels(self):
        """A subclass that does NOT implement number_of_wheels"""
        with ytest.raises(typeError):

            class Incomplete(Vehicle):
                pass

            Incomplete(
                Manufacturer("X", "Y"),
                AutoModel("Z", True, [2020]),
                25.0
            )

class TestSedan:
#Created the full test class for the Sedan.
    @pytest.fixture
    def civic(self):
        return Sedan(
            Manufacturer("Honda", "Japan"),
            AutoModel("Civic", False, [1996, 1997, 1998]),
            28.0,
        )
    
    def test_number_of_wheels(self, civic):
        assert civic.number_of_wheels() == 4

    def test_release_year(self, civic):
        assert civic.release_year == 1996

    def test_mpg(self, civic):
        assert civic.mpg == pytest.approx(28.0)

    def test_manufacturer(self, civic):
        assert civic.manufactuer.name == "Honda"
        assert civic.manufactuer.country == "Japan"

    def test_model_name(self, civic):
        assert civic.model.name == "Civic"

    def test_how_far_with(self, civic):
        assert civic.how_far_with(10) == pytest.approx(280.0)
        assert civic.how_far_with(0) == pytest.approx(0.0)

    def test_str_contains_required_parts(self, civic):
        s = str(civic)
        assert "(Honda, Japan)" in s
        assert "Civic" in s
        assert "28.00" in s

    def test_str_does_not_contain_dually(self, civic):
        s = str(civic)
        assert "dually" not in s.lower()

    def test_is_instance_of_vehicle(self, civic):
        assert isinstance(civic, Vehicle)

class TestTruck:
#Created the full test class for the Truck
    @pytest.fixture
    def f150(self):
        return Truck(
            Manufacturer("Ford","USA"),
            AutoModel("F150", True, [2020, 2021, 2022]),
            20.0,
            )
    
    @pytest.fixture
    def tundra_dually(self):
        return Truck(
            Manufacturer("toyota", "Japan"),
            AutoModel("Tundra", False, [1987, 1988]),
            30.0,
            is_dually=True,
        )
    
    #---default (not dually) ---

    def test_defualt_not_dually(self, f150):
        assert f150.is_dually is False

    def test_wheels_non_dually(self, f150):
        assert f150.number_of_wheels() == 4

    def test_release_year_f150(sself, f150):
        assert f150.release_year == 2020

    def test_str_non_dually(self, f150):
        s = str(f150)
        assert "(Ford, USA)" in s
        assert "F150" in s
        assert "20.00" in s
        assert "False" in s
    
    #---dually----

    def test_is_dually_true(self, tundra_dually):
        assert tundra_dually.is_dually is True
        
    def test_wheels_dually(self, tundra_dually):
        assert tundra_dually.number_of_wheels() == 6

    def test_release_year_tundra(self, tundra_dually):
        assert tundra_dually.release_year == 1987

    def test_str_dually(self, tundra_dually):
        s = str(tundra_dually)
        assert "(Toyota, Japan)" in s
        assert "Tundra" in s
        assert "30.00" in s
        assert "True" in s

    def test_how_far_with(self, tundra_dually):
        assert tundra_dually.how_far_with(5) == pytest.approx()

    def test_is_instance_of_vehicl(self, f150):
        assert isinstance(f150, Vehicle)

