from interface import SettingsPuzzle
from constants import *
from pint import UnitRegistry

def main():
    # print("Hello from personal-1!")

    # app = SettingsPuzzle()
    # app.run()

    ureg = UnitRegistry()
    length = CONT_40[0] * ureg.meter
    print(f"original length: {length}")
    print(f"meters to feet: {length.to("feet").magnitude}")


    if D430[0] > 1060:
      print("Long side is larger")

    footprint = D430[0] * ureg.mm
    print(footprint)
    fit_count = length / footprint.to("meter")
    print(f"how many will fit: {fit_count.magnitude}")

if __name__ == "__main__":
   main()
