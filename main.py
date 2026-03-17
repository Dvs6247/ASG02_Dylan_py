from manufacturer import Manufacturer
from auto_model import AutoModel
from sedan import Sedan
from truck import Truck
from garage import Garage

def main():
    #Created manufacturers
    ford = Manufacturer("Ford", "USA")
    honda = Manufacturer("Honda", "Japan")
    bmw = Manufacturer("BMW", "Germany")
    toyota = Manufacturer("Toyota", "Japan")

    #Created Models
    f150_model = AutoModel("F150", True, list(range(2020, 2023)))
    civic_model = AutoModel("Civic", False, list(range(1996, 1999)))
    m3_model = AutoModel("M3 Limited", False, list(range(2015, 2018)))
    tundra_model = AutoModel("Tundra", False, list(range(1987, 1990)))

    #Created vehicles
    f150 = Truck(ford, f150_model, 20.0)
    civic = Sedan(honda, civic_model, 298.0)
    m3 = Sedan(bmw, m3_model, 30.0)
    tundra = Truck(toyota, tundra_model, 30.0, is_dually=True)

    #Build and use the garage
    g = Garage()
    g.add_vehicl(f150)
    g.add_vehicle(civic)
    g.add_vehicle(m3)
    g.add_vehicle(tundra)

    print("Before sorting:")
    print(g)
    print()

    g.sort_by_release_year()

    print("After sorting:")
    print(g)


if __name__ == "__main__":
    main()
    