from interface import SettingsPuzzle
from constants import *
from pint import UnitRegistry

def main():
    # print("Hello from personal-1!")

    # app = SettingsPuzzle()
    # app.run()

    ureg = UnitRegistry()

    #TODO the container size should be chosen by the user
    container_size = CONT_40
    container_label = "40' Container"
    
    #TODO these values should use appropriate conversions based on container units
    length = container_size[0] * ureg.meter
    width = container_size[1] * ureg.meter
    height = container_size[2] * ureg.meter
    
    print(f"original length: {length}")
    print(f"meters to feet: {length.to("feet").magnitude}")


    #TODO the pallet model should be chosen by the user
    pallet_model = D430
    if pallet_model[0] > 1060:
      print("Long side is larger")

    footprint_L = pallet_model[0] * ureg.mm
    fit_count_L = length // footprint_L.to("meter")
    print(f"how many will fit (length): {fit_count_L.magnitude}")

    footprint_S = pallet_model[1] * ureg.mm
    fit_count_S = width // footprint_S.to("meter")
    print(f"how many will fit (width): {fit_count_S.magnitude}")

    footprint_H = pallet_model[2] * ureg.mm
    fit_count_H = height // footprint_H.to("meter")
    print(f"how tall can the stack be: {fit_count_H.magnitude}")

    fit_count_stacks = fit_count_L.magnitude * fit_count_S.magnitude
    print(f"You can fit {fit_count_stacks} stacks in a {container_label}.")
    fit_count_total = fit_count_stacks * fit_count_H.magnitude
    print(f"That means you can fit {fit_count_total} pallets in a {container_label}.")

if __name__ == "__main__":
   main()
