import numpy as np
import math
from collections import defaultdict


def read(filename):
    G = {}
    for l in open(filename):
        tokens = l.strip().split()
        device = tokens[0][:-1]
        output = tokens[1:]
        G[device] = output
    return G


def main(filename):
    G = read(filename)
    print(G)

    count = 0
    Q = ["you"]
    while Q:
        u = Q.pop(0)
        print(u)
        if u == "out":
            count += 1
            print("OUT")
            continue
        Q += G[u]
    print(count)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("input", nargs="?", default="input.txt")
    args = parser.parse_args()
    main(args.input)
