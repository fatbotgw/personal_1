from interface import SettingsPuzzle
from constants import *  # noqa: F403
from pint import UnitRegistry

def fit_count(pallet_dim, container_dim, unitreg, p_units):
    """Calculates number of stacks in the container dimension."""
    if p_units == "mm":
        units = unitreg.mm
    elif p_units == "inch":
        units = unitreg.inch
    elif p_units == "feet":
        units = unitreg.feet
    else:
        units = unitreg.meter

    footprint = pallet_dim * units

    return container_dim // footprint.to("meter")


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

    #TODO the pallet model should be chosen by the user
    pallet_model = D322
    if pallet_model[0] > 1060:
      print("Long side is larger")

    # this is the length of the trailer/container
    fit_count_L = fit_count(pallet_model[0], length, ureg, pallet_model[3])
    print(f"how many will fit (length): {fit_count_L.magnitude}")

    # this is the width of the trailer/container
    fit_count_S = fit_count(pallet_model[1], width, ureg, pallet_model[3])
    print(f"how many will fit (width): {fit_count_S.magnitude}")

    # this is the height of the trailer/container
    fit_count_H = fit_count(pallet_model[2], height, ureg, pallet_model[3])
    print(f"how tall can the stack be: {fit_count_H.magnitude}")


    fit_count_stacks = fit_count_L.magnitude * fit_count_S.magnitude
    print(f"You can fit {fit_count_stacks} stacks in a {container_label}.")
    fit_count_total = fit_count_stacks * fit_count_H.magnitude
    print(f"That means you can fit {fit_count_total} pallets in a {container_label}.")

if __name__ == "__main__":
   main()
