from interface import SettingsPuzzle
from constants import *  
from pint import UnitRegistry

def unit_checker(pallet_units, unitreg):
    if pallet_units == "mm":
        units = unitreg.mm
    elif pallet_units == "inch":
        units = unitreg.inch
    elif pallet_units == "feet":
        units = unitreg.feet
    else:
        units = unitreg.meter

    return units


def fit_count(pallet_dim, container_dim, unitreg, p_units):
    """Calculates number of stacks in the container dimension."""
    footprint = pallet_dim * unit_checker(p_units, unitreg)

    return container_dim // footprint.to("meter")


def find_all_arrangements(container,pallet, unitreg):
    """Find all possible mixed arrangements"""
    arrangements = []

    container_l = (container[0] * unitreg.meter).to("mm")
    container_w = (container[1] * unitreg.meter).to("mm")
    p_long = (pallet[0] * unit_checker(pallet[3], unitreg)).to("mm")
    p_short = (pallet[1] * unit_checker(pallet[3], unitreg)).to("mm")

    container_h = container[2] * unitreg.meter
    p_height = (pallet[2] * unit_checker(pallet[3], unitreg)).to("mm")
    layers = int(container_h // p_height)

    
    # Define both orientations as "strips" that run the full length of container
    orientations = [
        {'name': 'L', 'strip_width': p_short, 'pallets_per_strip': container_l // p_long},
        {'name': 'W', 'strip_width': p_long, 'pallets_per_strip': container_l // p_short}
    ]
    
    # Calculate maximum strips for each orientation that fit across container width
    max_strips = {}
    for orient in orientations:
        max_strips[orient['name']] = int(container_w // orient['strip_width'])
    
    # Try every combination of L-strips and W-strips
    for strips_L in range(max_strips['L'] + 1):
        for strips_W in range(max_strips['W'] + 1):
            if strips_L == 0 and strips_W == 0:
                continue # Skip empty arrangement
            
            # Calculate total width used by this combination
            total_width = (strips_L * orientations[0]['strip_width'] + 
                         strips_W * orientations[1]['strip_width'])
            
            # Only keep arrangements that fit in container
            if total_width <= container_w:
                # Calculate total pallets in this arrangement
                total_pallets = (strips_L * orientations[0]['pallets_per_strip'] + 
                               strips_W * orientations[1]['pallets_per_strip'])
                
                waste_width = container_w - total_width
                pattern = 'L' * strips_L + 'W' * strips_W # Visual pattern like "LLW"
                
                arrangements.append({
                    'L_strips': strips_L,
                    'W_strips': strips_W,
                    'total_pallets': total_pallets,
                    'used_width': total_width,
                    'waste_width': waste_width,
                    'pattern': pattern,
                    'efficiency': (total_width / container_w) * 100
                })
    
    best = max(arrangements, key=lambda x: x['total_pallets'])
    # Calculate total pallets across all layers
    total_pallets = best['total_pallets'] * layers

    # return arrangements
    return create_result(
            pallet, total_pallets, layers, best['total_pallets'], 
            best['pattern'], best['waste_width'], container, pallet
        )

def create_result(pallet, total_pallets, layers, pallets_per_layer, 
                      pattern, waste_width, container, pallet_dims):
        """Create standardized result dictionary"""
        return {
            'pallet_name': pallet,
            'total_pallets': int(total_pallets),
            'layers': int(layers),
            'pallets_per_layer': int(pallets_per_layer),
            'arrangement_pattern': pattern,
            'waste_width_mm': waste_width,
            'container_dims': container,
            'pallet_dims': pallet_dims,
            # 'efficiency_percent': ((container_dims[0] * 1000 - waste_width) / (container_dims[0] * 1000)) * 100 if container_dims[0] > 0 else 0
        }

def main():
    # print("Hello from personal-1!")

    # app = SettingsPuzzle()
    # app.run()

    ureg = UnitRegistry()

    #TODO the container size should be chosen by the user
    container_size = CONT_40
    container_label = container_size[4]
    
    #TODO the pallet model should be chosen by the user
    pallet_model = D430


    arrangements = find_all_arrangements(container_size, pallet_model, ureg)
    # print(arrangements)

    print(f"You can fit {arrangements['total_pallets']} total pallets in the container.")
    print(f"You should use the following arrangement: {arrangements['arrangement_pattern']}")

    # # this is the length of the trailer/container
    # fit_count_L = fit_count(pallet_model[0], length, ureg, pallet_model[3])
    # print(f"how many will fit (length): {fit_count_L.magnitude}")

    # # this is the width of the trailer/container
    # fit_count_S = fit_count(pallet_model[1], width, ureg, pallet_model[3])
    # print(f"how many will fit (width): {fit_count_S.magnitude}")

    # # this is the height of the trailer/container
    # fit_count_H = fit_count(pallet_model[2], height, ureg, pallet_model[3])
    # print(f"how tall can the stack be: {fit_count_H.magnitude}")


    # fit_count_stacks = fit_count_L.magnitude * fit_count_S.magnitude
    # print(f"You can fit {fit_count_stacks} stacks in a {container_label}.")
    # fit_count_total = fit_count_stacks * fit_count_H.magnitude
    # print(f"That means you can fit {fit_count_total} pallets in a {container_label}.")

if __name__ == "__main__":
   main()
