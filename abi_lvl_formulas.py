# 2 dictionaries that hold constants for calculating digimon abi gains
# one will be for digivolution, other for de-digivolution
# ...
# yes, there's literally a formula for this on Cyber Sleuth


import math

# dictionary for digivolution abi constants
digivolve_abi_constants = {
  "Training 1": 0,
  "Training 2": 1,
  "Rookie": 1,
  "Champion": 2,
  "Ultimate": 2,
  "Mega": 3
}

# dictionary for de-digivolution abi constants
de_digivolve_abi_constants = {
  "Training 2": 1,
  "Rookie": 2,
  "Champion": 3,
  "Ultimate": 4,
  "Mega": 5,
  "Ultra": 6
}

# dictionary for base level caps per stage
base_level_per_stage = {
    "Training 1": 5,
    "Training 2": 9,
    "Rookie": 15,
    "Champion": 25,
    "Ultimate": 40,
    "Mega": 60
}

# dictionary for GenUp constants per stage
genup_constants_per_stage = {
    "Training 1": 3,
    "Training 2": 6,
    "Rookie": 9,
    "Champion": 12,
    "Ultimate": 15,
    "Mega": 18
}

 # dictionary for GenDown constants per stage
gendown_constants_per_stage = {
    "Training 1": 0,
    "Training 2": 1,
    "Rookie": 1,
    "Champion": 2,
    "Ultimate": 2,
    "Mega": 3
}

def calculate_abi_gain(stage, level, transition_type):
    # stage: current stage of the digimon (Training 1, Training 2, Rookie, Champion, Ultimate, Mega)
    # level: current level of the digimon
    # transition_type: either "digivolve" or "de-digivolve"

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

def calculate_new_max_level (current_max, current_stage, target_stage, level, transition_type):
    # current_max: current max lvl of the digimon
    # current_stage: base lvl stage of current digimon
    # target_stage: base lvl stage of target digimon
    # level: current level of the digimon
    # transition_type: either "digivolve" or "de-digivolve"
    
    current_base = base_level_per_stage[current_stage]
    target_base = base_level_per_stage[target_stage]

    if transition_type == "digivolve":
        genup_constant = genup_constants_per_stage[current_stage]
        return current_max - current_base + target_base + math.floor(level/5) + genup_constant
    elif transition_type == "de-digivolve":
        gendown_constant = gendown_constants_per_stage[current_stage]
        if current_stage in ["Training 2", "Champion", "Mega"]:
        # x = constant used if digimon is of a certain stage
            x = 5
        else:
            x = 0
        return current_max - current_base + target_base + math.floor((level+x)/10) + gendown_constant
    else:
        raise ValueError("Invalid transition type. Must be 'digivolve' or 'de-digivolve'.")

# Test cases
# result = calculate_new_max_level(30, "Rookie", "Champion", 20, "digivolve") result should be 53
# print(result)