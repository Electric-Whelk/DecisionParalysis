import random
import sys


def get_random_number(length: int):
    return random.randint(0, (options_count - 1))

def format_and_print(input: str):
    print(input.strip())



with open(sys.argv[1]) as f:
    lines = f.readlines()
    options_count = len(lines)
    rand = get_random_number(options_count)
    format_and_print(lines[rand])





        