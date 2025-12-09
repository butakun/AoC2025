import numpy as np
from collections import defaultdict


def read(filename):
    tiles = [[int(v) for v in l.strip().split(",")] for l in open(filename)]
    return tiles


def main(filename):
    tiles = read(filename)
    print(tiles)

    N = len(tiles)
    amax = None
    for i in range(N):
        p1 = tiles[i]
        for j in range(i+1, N):
            p2 = tiles[j]
            dx = abs(p2[0] - p1[0]) + 1
            dy = abs(p2[1] - p1[1]) + 1
            a = dx * dy
            print(f"{i=}, {j=}, {p1=}, {p2=}, {a=}, {amax=}")
            if amax is None or amax < a:
                amax = a
    print(amax)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("input", nargs="?", default="input.txt")
    args = parser.parse_args()
    main(args.input)
