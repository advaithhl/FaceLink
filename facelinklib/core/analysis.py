import networkx as nx


def shortest_link(g: nx.MultiGraph, person1, person2):
    try:
        sp = nx.shortest_path(g, person1, person2)
        return sp
    except nx.exception.NodeNotFound as mpe:
        print(mpe)
