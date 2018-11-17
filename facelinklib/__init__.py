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

if RUN_MODE == 2 and not RESULTS.exists():
        print('- You are trying to analyse photos without providing results from the first stage.')
        print('- Please give a folder containing pictures, so that I can identify faces from them.')
        print('- You can start analysis after I identify the faces.')
        exit()

print("+ Using {} as results folder".format(RESULTS))
