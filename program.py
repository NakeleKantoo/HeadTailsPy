#!/bin/python3
import random

def main():
    result = random.choice(['Heads!', 'Tails!'])
    print('The result is: ' + result + '\n')
    if input('Roll again? (y/N): ') == 'y':
        main()
    else:
        quit()

main()
