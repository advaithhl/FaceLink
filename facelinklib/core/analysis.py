import networkx as nx

from facelinklib.util.person import Person


def shortest_link(g: nx.MultiGraph, person1, person2):
    try:
        sp = nx.shortest_path(g, person1, person2)
        return sp
    except nx.exception.NodeNotFound as mpe:
        print(mpe)


def get_links_between(g, person1, person2):
    links = g[person1][person2]
    return (links[i]['photo'] for i in range(len(links)))


def get_all_related_people(g: nx.MultiGraph, person):
    return g.neighbors(person)


def get_all_people(g):
    return (person for person in g.nodes)
