from pathlib import Path
from sys import argv

HOME = Path('.')
RESULTS = Path('{}/results/'.format(HOME))


def results_dir_safe():
    cnt = 2
    global RESULTS
    while RESULTS.exists():
        RESULTS = Path('{}/results{}/'.format(HOME, str(cnt)))
        cnt += 1
    if len(argv) < 2:
        cnt -= 2
        RESULTS = Path('{}/results{}/'.format(HOME, str(cnt)))
    print("+ Using folder {} as results folder".format(RESULTS))


results_dir_safe()
