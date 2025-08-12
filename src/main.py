from interface import SettingsPuzzle
from constants import *
from pint import UnitRegistry

def main():
    # print("Hello from personal-1!")

    # app = SettingsPuzzle()
    # app.run()

    ureg = UnitRegistry()
    length = CONT_40[0] * ureg.meter
    width = CONT_40[1] * ureg.meter
    print(f"original length: {length}")
    print(f"meters to feet: {length.to("feet").magnitude}")


    if D430[0] > 1060:
      print("Long side is larger")

    footprint_L = D430[0] * ureg.mm
    print(footprint_L)
    fit_count_L = length // footprint_L.to("meter")
    print(f"how many will fit (length): {fit_count_L.magnitude}")

    footprint_S = D430[1] * ureg.mm
    print(footprint_S)
    fit_count_S = width // footprint_S.to("meter")
    print(f"how many will fit (width): {fit_count_S.magnitude}")


if __name__ == "__main__":
   main()
