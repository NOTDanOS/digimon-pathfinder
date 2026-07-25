from main import build_graph, find_path

#build_graph tests

def test_build_graph_empty():
    #empty dictionary test
    digimon_list = []
    result = build_graph(digimon_list)
    assert result == {}

def test_build_graph_basic():
    #regular dictionary test
    digimon_list = [
        {"name": "Agumon", "stage": "Rookie", "evolves_to": ["Greymon"], "evolves_from": ["Koromon"]},
        {"name": "Greymon", "stage": "Champion", "evolves_to": ["MetalGreymon"], "evolves_from": ["Agumon"]},
        {"name": "Koromon", "stage": "Training 2", "evolves_to": ["Agumon"], "evolves_from": []}
    ]

    result = build_graph(digimon_list)

    assert result == {
        "Agumon": {"name": "Agumon", "stage": "Rookie", "evolves_to": ["Greymon"], "evolves_from": ["Koromon"]},
        "Greymon": {"name": "Greymon", "stage": "Champion", "evolves_to": ["MetalGreymon"], "evolves_from": ["Agumon"]},
        "Koromon": {"name": "Koromon", "stage": "Training 2", "evolves_to": ["Agumon"], "evolves_from": []}
    }

#find_path tests

def test_find_path_empty():
    #empty graph test
    graph = {}
    result = find_path(graph, "Agumon", "Greymon")
    assert result is None

def test_find_path_basic():
    #basic pathfinding test
    digimon_list = [
        {"name": "Agumon", "stage": "Rookie", "evolves_to": ["Greymon"], "evolves_from": ["Koromon"]},
        {"name": "Greymon", "stage": "Champion", "evolves_to": ["MetalGreymon"], "evolves_from": ["Agumon"]},
        {"name": "Koromon", "stage": "Training 2", "evolves_to": ["Agumon"], "evolves_from": []}
    ]

    graph = build_graph(digimon_list)
    result = find_path(graph, "Koromon", "Greymon")

    assert result == [
        {"name": "Koromon", "transition": None},
        {"name": "Agumon", "transition": "digivolve"},
        {"name": "Greymon", "transition": "digivolve"}
    ]

def test_find_path_no_path():
    # test for no path found
    # if digimon is in evolved_from but not evolved_to (and the opposite), throw error
    digimon_list = [
        {"name": "Agumon", "stage": "Rookie", "evolves_to": ["Greymon"], "evolves_from": []},
        {"name": "Greymon", "stage": "Champion", "evolves_to": ["MetalGreymon"], "evolves_from": ["Agumon"]},
        {"name": "Koromon", "stage": "Training 2", "evolves_to": ["Agumon"], "evolves_from": []}
    ]

    graph = build_graph(digimon_list)
    result = find_path(graph, "Greymon", "Koromon")

    assert result is None