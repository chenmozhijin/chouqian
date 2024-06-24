import argparse
import time

import main

parser = argparse.ArgumentParser()
parser.add_argument('--task', choices=['get_version', 'get_year'], required=True)
arg = parser.parse_args()

version = ".".join([i.split("-")[0] for i in main.__version__.replace("v", "").split(".")])

year = time.strftime("%Y")
if year != '2024':
    year = "2024-" + year

match arg.task:
    case 'get_version':
        print(version)
    case 'get_year':
        print(year)
