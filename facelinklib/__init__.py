from pathlib import Path
from sys import argv

HOME = Path('.')
RESULTS = Path('{}/results/'.format(HOME))
if len(argv) < 2:
    RUN_MODE = 2
else:
    RUN_MODE = 1


if RUN_MODE == 1:
    while RESULTS.exists():
        print("A folder named {} exists. This might interfere with my work.".format(RESULTS))
        print("I can use another folder to save results.")
        new_name = input("Please enter another name for the results folder : ")
        RESULTS = HOME.joinpath(new_name)

print("+ Using {} as results folder".format(RESULTS))
