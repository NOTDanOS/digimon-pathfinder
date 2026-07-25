from collections import deque
import json

from abi_lvl_formulas import calculate_abi_gain, calculate_new_max_level


def build_graph(digimon_list):
  # PURPOSE
  # grabs a JSON file of digimons (look at digimon_data.json) and maps them into a dictionary of dictionaries, 
  # where the key is the digimon name and the value is the digimon's data (stage, evolves_to, evolves_from, etc.)
  # the keys for inner dictionaries are the data themselves: "name", "stage", "evolves_to", "evolves_from, etc."
  # 
  # PARAMETERS
  # digimon_list: list of dictionaries, each dictionary contains data for a digimon
  graph = {}
  for entry in digimon_list:
     graph[entry["name"]] = entry
  return graph

def find_path(graph, start, end):
    # PURPOSE
    # finds a path from one digimon to another, if it exists, using BFS (for now)
    # 
    # OUTPUT
    # list of dictionaries, each dictionary contains the name of a digimon and the transition type
    # 
    # PARAMETERS
    # graph: dictionary of digimon
    # start: name of starting digimon
    # end: name of ending digimon

    # checks if digimon (start or end) is in the graph, if not return None
    if start not in graph or end not in graph:
        return None
    
    queue = deque()
    queue.append([{"name": start, "transition": None}])
    visited = set()

    while queue:
        path = queue.popleft()
        current = path[-1] # last digimon in the path

        if current["name"] == end: # we found the digimon we want
            return path

        if current["name"] in visited: #
            continue
        visited.add(current["name"])

        for neighbor in graph[current["name"]]["evolves_to"]:
            if neighbor not in visited and neighbor in graph:  # check if neighbor digimon has an entry in the graph
                new_path = list(path)
                new_path.append({"name": neighbor, "transition": "digivolve"})  # this loop focuses on DIGIVOLVING UP
                queue.append(new_path)
        
        for neighbor in graph[current["name"]]["evolves_from"]:
            if neighbor not in visited and neighbor in graph:  # check if neighbor digimon has an entry in the graph
                new_path = list(path)
                new_path.append({"name": neighbor, "transition": "de-digivolve"})  # this loop focuses on DIGIVOLVING DOWN
                queue.append(new_path)
        
    return None  # no path found

def check_abi_validity(path, graph, starting_abi, starting_max_level):
    # checks if digimon has enough validity to reach wanted stage by passing each stat through "gates"
    #
    # OUTPUT: boolean
    #
    # PARAMETERS
    # path: list of dicts, from starting digimon to target digimon, each dict contains name and transition
    # graph: dictionary of digimon
    # starting_abi: current abi of the digimon
    # starting_max_level: current max level of the digimon

    for i in range(len(path)-1):
        current_digimon = path[i]["name"]
        next_digimon = path[i+1]["name"]
        transition_type = path[i+1]["transition"]
        current_stage = graph[current_digimon]["stage"]
        next_stage = graph[next_digimon]["stage"]
        required_level = graph[next_digimon]["requirements_to_reach"]["level"]
        required_abi = graph[next_digimon]["requirements_to_reach"]["ABI"]

        # check if new abi is valid for the next stage
        if starting_abi < required_abi:
            return False  # not enough abi to reach the next stage

        # check if new max level is valid for the next stage
        if starting_max_level < required_level:
            return False  # not enough max level to reach the next stage

        # calculate new max level
        new_max_level = calculate_new_max_level(starting_max_level, current_stage, next_stage, required_level, transition_type)
                
        # calculate new abi
        new_abi_gain = calculate_abi_gain(current_stage, required_level, transition_type)

        # update starting values for the next iteration
        starting_abi += new_abi_gain
        starting_max_level = new_max_level

    return True  # all checks passed, path is valid

# quick test cases for build_graph and find_path functions w/ json file
if __name__ == "__main__":
    with open ("digimon_data.json") as f:
        data = json.load(f)
    digimon_graph = build_graph(data["digimon"])

    result = find_path(digimon_graph, "Garurumon", "Pabumon")
    print(result) #test for de-digivolution

    result = find_path(digimon_graph, "Pabumon", "Garurumon")
    print(result) #test for digivolution

    #next step: make basic BFS to grab appropriate digimon AFTER