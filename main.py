import json

with open ("digimon_data.json") as f:
    data = json.load(f)

# grabs a JSON file of digimons (look at digimon_data.json) and maps them into a dictionary
def build_graph(digimon_list):
  graph = {}
  for entry in digimon_list:
     graph[entry["name"]] = entry
  return graph

digimon_graph = build_graph(data["digimon"])

print(digimon_graph["Garurumon"])

#next step: make basic BFS to grab appropriate digimon AFTER