#!/usr/local/bin/python3

import sys

def find_capital(state):
    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }
    if state in states.keys():
        return capital_cities.get(states.get(state))
    return 'Unknown state'

def main():
    if len(sys.argv) == 2:
        print(find_capital(sys.argv[1]))


if __name__ == '__main__':
    main()