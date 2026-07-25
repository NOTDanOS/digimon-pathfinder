from collections import deque
import json

with open ("digimon_data.json") as f:
    data = json.load(f)

# grabs a JSON file of digimons (look at digimon_data.json) and maps them into a dictionary
def build_graph(digimon_list):
  graph = {}
  for entry in digimon_list:
     graph[entry["name"]] = entry
  return graph

def find_path(graph, start, end):
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
    # checks if digimon has enough validity to reach wanted stage
    # graph: dictionary of digimon
    # path: list of dicts, from starting digimon to target digimon, each dict contains name and transition
    # starting_abi: current abi of the digimon
    # starting_max_level: current max level of the digimon
    current_stage = graph[path[0]["name"]]["stage"]
    pass

digimon_graph = build_graph(data["digimon"])

result = find_path(digimon_graph, "Garurumon", "Pabumon")
print(result) #test for de-digivolution

result = find_path(digimon_graph, "Pabumon", "Garurumon")
print(result) #test for digivolution

#next step: make basic BFS to grab appropriate digimon AFTER