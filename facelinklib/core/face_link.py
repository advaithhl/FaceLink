from itertools import combinations
from pathlib import Path

import networkx as nx

from facelinklib import RESULTS
from facelinklib.util.person import Person


def get_people(path: Path):
    """
    Yield portraits as Person objects in a directory. Person objects are
    created from the portraits found in the various subfolders of param path.

    :param path: Directory containing the pictures
    :return: generator object which yields Person(s)
    """

    return (Person(pname.name.split('.')[0]) for pname in path.iterdir() if pname.is_file() and pname.name not in ['.DS_Store'])


def get_photo_path(results: Path):
    """
    Yield photo paths.
    This function iterates the results folder created by store_faces() method 
    and yields paths of the folders formed from the photos.

    :param results: Directory created by store_faces() method
    :return: generator object which yields photo paths.
    """

    return (photo for photo in results.iterdir() if photo.is_dir())


def make_graph():
    """
    Make a Networkx Graph from the portraits created.
    Nodes are of type person and edges are added if 2 Person(s) appear on a 
    folder together.

    :return: networkx graph representing connections between people
    """
    person_graph = nx.Graph()
    for photo_path in get_photo_path(RESULTS):
        for (person1, person2) in combinations(get_people(photo_path), 2):
            person_graph.add_edge(person1, person2)
    return person_graph
