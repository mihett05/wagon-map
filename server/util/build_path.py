import json
import os

from networkx import node_link_graph, shortest_path


with open(f"{os.path.dirname(os.path.realpath(__file__))}/../static_data/graph.json") as graph_file:
    json_data = json.load(graph_file)
    nx_graph = node_link_graph(json_data)


def get_shortest_path(node_1: int, node_2: int) -> list[int]:
    return shortest_path(nx_graph, node_1, node_2, weight="weight")
