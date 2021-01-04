import argparse
from bin_search import find_index as binary 
from linear import find_index as linear
from typing import List

def main(args: argparse.Namespace) -> None:
    algorithms = {
            'binary' : binary,
            'linear' : linear,
        }
    print(f'algorithm = {args.algorithm}, path = {args.path}, search term = {args.search_term}')
    load_names(args.path)

    benchmark(algorithms[args.algorithm],load_names(args.path),args.search_term)

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
            '-a','--algorithm', choices=('binary','linear')
            )
    parser.add_argument('-f',dest='path')
    parser.add_argument('search_term',)
    return parser.parse_args()

def load_names(path):
    print(f'opening file {path}', end = '\n', flush = True )
    with open(path) as file:
        names = file.read().splitlines()
        print('file reading complete...')
        return names

def benchmark(algorithm, elements: List[str], value: str ) -> None:
    print(algorithm(elements,value))


if __name__ == "__main__":
    try:
        main(parse_args())
    except KeyboardInterrupt:
        print("KeyboardInterrupt.............")
