import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Pull data from the Yu-Gi-Oh! Forbidden and Limited List.')

    parser.add_argument('-a', '--all', help='get the entire list', action='store_true')
    parser.add_argument('-d', '--diff', help='get only what changed on the most recent list', action='store_true')
    parser.add_argument('-f', '--forbidden', help='get newly forbidden cards', action='store_true')
    parser.add_argument('-l', '--limited', help='get newly limited cards', action='store_true')
    parser.add_argument('-s', '--semi-limited', help='get newly semi-limited cards', action='store_true')
    parser.add_argument('-u', '--unlimited', help='get cards no longer on the list', action='store_true')
    parser.add_argument('-c', '--clear-cache', help='manually clear the cache', action='store_true')
    parser.add_argument('-o', '--output-format', help='choose an output format', default='table', choices=['table', 'json'])

    return parser.parse_args()
