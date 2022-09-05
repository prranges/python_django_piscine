#!/usr/local/bin/python3

import sys

def find_capital(arg):

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

    if arg in states.keys():
        return capital_cities.get(states.get(arg)) + ' is the capital of ' + arg

    for key_city, value_city in capital_cities.items():
        if value_city == arg:
            for key_state, value_state in states.items():
                if value_state == key_city:
                    return arg + ' is the capital of ' + key_state
    return arg + ' is neither a capital city nor a state'

def main():
    if len(sys.argv) == 2:
        arg_list = sys.argv[1].title().split(',')
        for arg in arg_list:
            arg = arg.strip()
            if arg:
                print(find_capital(arg))


if __name__ == '__main__':
    main()