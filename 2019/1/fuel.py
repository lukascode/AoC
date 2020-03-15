#!/usr/bin/env python3

import sys
from math import floor

def calcFuel(mass):
    fuel = floor(mass / 3) - 2.0
    if fuel > 0:
        return fuel + calcFuel(fuel)
    return 0

try:
    with open('input') as f:
        data = f.readlines()
    data = list(map(lambda x: int(x), data))
    totalFuel = 0
    for mass in data:
        fuel = calcFuel(mass)
        totalFuel += fuel
    print("TotalFuel", totalFuel)
except IOError as e:
    sys.stderr.write(str(e) + '\n')

