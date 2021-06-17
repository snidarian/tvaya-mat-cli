#!/usr/bin/python3

import requests as rq
import argparse
from colorama import Fore, Style


# ansi color definitions
green = Fore.GREEN
red = Fore.RED
yellow = Fore.YELLOW
reset = Fore.RESET

parser = argparse.ArgumentParser(description="Returns 'Yo momma' jokes from web API")

args = parser.add_argument('-c', '--count', help='Specify how many yo momma jokes are required', type=int, default=1)

args = parser.parse_args()


result = rq.get(f'https://yomomma-api.herokuapp.com/jokes?count={args.count}')

python_object_from_json = result.json()

index = 1
for joke in python_object_from_json:
    print(f'{index}. ', end='')
    print(yellow + joke['joke'] + reset)
    index+=1










