import numpy as np
import math
from collections import defaultdict


def read(filename):
    machines = []
    for l in open(filename):
        tokens = l.split(" ")
        lights, wirings = tokens[0][1:-1], tokens[1:-1]

        lights = [l == "#" for l in list(lights)]
        lights_bin = sum([bit << i for i, bit in enumerate(lights)])

        wirings = [[int(v) for v in w[1:-1].split(",")] for w in wirings]
        wirings_bin = [sum([1 << i for i in w]) for w in wirings]

        print(f"{lights=}, {lights_bin=}, {wirings=}, {wirings_bin=}")
        machines.append((lights_bin, wirings_bin))
    return machines


def configure(lights, wirings):
    G = defaultdict(dict)
    H = {0: 0}
    Q = [(0, w) for w in wirings]
    best = None
    while Q:
        u = Q.pop(0)
        l, w = u
        out = l ^ w
        G[l][w] = out
        #print(f"{l=},{w=},{out=}")

        v = H[l] + 1

        if out == lights:  # GOAL
            if best is None:
                best = v
            else:
                best = min(best, v)
            print(f"{best=}")

        if out in H:
            if v < H[out]:
                H[out] = v
        else:
            H[out] = v

        if best is None or v < best - 1:
            if out not in G:
                Q += [(out, w) for w in wirings if (out ^ lights) & w]

    #print(f"{dict(G)=}")
    #print(f"{H=}")
    return H[lights]


def main(filename):
    machines = read(filename)
    print(machines)

    sum = 0
    for lights, wirings in machines:
        print(f"MACHINE {lights}, {wirings}")
        counts = configure(lights, wirings)
        sum += counts
        print(f"  {counts=}")
        print()
    print(f"{sum=}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("input", nargs="?", default="input.txt")
    args = parser.parse_args()
    main(args.input)
