#!/usr/local/bin/python3

import sys

def find_capital(city):
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
    for key_city, value_city in capital_cities.items():
        if value_city == city:
            for key_state, value_state in states.items():
                if value_state == key_city:
                    return key_state
    return 'Unknown capital city'

def main():
    if len(sys.argv) == 2:
        print(find_capital(sys.argv[1]))


if __name__ == '__main__':
    main()