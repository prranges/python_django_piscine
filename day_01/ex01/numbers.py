#!/usr/local/bin/python3

def num_print():
    f = open('numbers.txt', 'r')
    num_str = f.read()
    num_list = num_str.split(',')
    for num in num_list:
        print(num)

if __name__ == '__main__':
    num_print()

