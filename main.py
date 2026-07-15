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
    queue = deque()
    queue.append([start])
    visited = set()

    while queue:
        path = queue.popleft()
        current = path[-1] # last digimon in the path

        if current == end: # we found the digimon we want
            return path

        if current in visited: #
            continue
        visited.add(current)

        for neighbor in graph[current]["evolves_to"]:
            if neighbor not in visited and neighbor in graph:  # check if neighbor digimon has an entry in the graph
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
        
        # now: look at current's neighbors (evolves_to)
        # for each neighbor not yet visited, build a new path and add it to the queue
        
    return None  # no path found

digimon_graph = build_graph(data["digimon"])

result = find_path(digimon_graph, "Pabumon", "Garurumon")
print(result)

#next step: make basic BFS to grab appropriate digimon AFTER