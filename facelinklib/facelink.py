from pathlib import Path
from sys import argv

from facelinklib import RESULTS, RUN_MODE
from facelinklib.core.analysis import *
from facelinklib.core.face_find import detect_faces, get_photos, store_faces
from facelinklib.core.face_link import make_graph
from facelinklib.util.person import Person


def print_menu():
    print()
    print('1. Find shortest path from person 1 to person 2')
    print('2. Find all links between person 1 and person 2')
    print('3. Find all people related to a person')
    print('4. Name all people')
    print('0. Exit')

    return int(input('\nChoice : '))


def _stage1():
    try:
        pics_path = Path(argv[1])
    except IndexError as ie:
        print('- You have not provided a path to look for pictures!')
        exit(-1)
    if not pics_path.exists():
        print("- I could not find a folder named '{}'".format(pics_path))
        exit(-1)

    for photo in get_photos(pics_path):
        face_locations = detect_faces(photo)
        store_faces(photo, face_locations)

    print("+ I have organised the portraits into subfolders in the results folder.")


def _stage2():
    g = make_graph()
    choice = print_menu()
    if choice == 1:
        person1_name = input('\nEnter person 1 name : ')
        person2_name = input('Enter person 2 name : ')
        s_path = shortest_link(g, Person(person1_name), Person(person2_name))
        if not s_path:
            print('No route found')
        else:
            print(s_path)
    elif choice == 2:
        person1_name = input('\nEnter person 1 name : ')
        person2_name = input('Enter person 2 name : ')
        if not g.has_edge(Person(person1_name), Person(person2_name)):
            print('No links found')
        else:
            print('I found link(s) between {} and {}'.format(person1_name, person2_name))
            link_gen = get_links_between(g, Person(person1_name), Person(person2_name))
            print('They appear together in the photos below')
            for link in link_gen:
                print(link)
    elif choice == 3:
        person_name = input('\nEnter name of the person : ')
        if not g.has_node(Person(person_name)):
            print('{} was not found in the network!'.format(person_name))
        else:
            print("Listing people related to '{}'".format(person_name))
            for i in get_all_related_people(g, Person(person_name)):
                print(i)
    elif choice == 4:
        print('\nListing every person in the network')
        for i in get_all_people(g):
            print('+', i)
    else:
        print('Exiting program with exit signal!')
        exit()


def main():
    if RUN_MODE == 1:
        print('+ Parsing the folder containing pictures from argument given...')
        _stage1()
    elif RUN_MODE == 2:
        print('+ Starting analysis from {} folder...'.format(RESULTS))
        _stage2()
    else:
        print('Invalid RUN MODE')
        exit(-1)

