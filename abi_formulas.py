# 2 dictionaries that hold constants for calculating digimon abi gains
# one will be for digivolution, other for de-digivolution
# ...
# yes, there's literally a formula for this on Cyber Sleuth


import math


digivolve_abi_constants = {
  "Training 1": 0,
  "Training 2": 1,
  "Rookie": 1,
  "Champion": 2,
  "Ultimate": 2,
  "Mega": 3
}

de_digivolve_abi_constants = {
  "Training 2": 1,
  "Rookie": 2,
  "Champion": 3,
  "Ultimate": 4,
  "Mega": 5,
  "Ultra": 6
}

def calculate_abi_gain(stage, level, transition_type):
    if transition_type == "digivolve":
        constant = digivolve_abi_constants[stage]
        if stage in ["Training 1", "Rookie", "Ultimate"]:
            formula = (level+5)/10
        else:
            formula = level/10
        return math.floor(constant + formula)
    elif transition_type == "de-digivolve":
        constant = de_digivolve_abi_constants[stage]
        return math.floor(constant + level/5)
    else:
        raise ValueError("Invalid transition type. Must be 'digivolve' or 'de-digivolve'.")

# Test cases
# result = calculate_abi_gain("Rookie", 10, "digivolve")
# print(result)