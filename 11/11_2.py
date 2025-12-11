import numpy as np
import math
from collections import defaultdict, deque


def read(filename):
    G = {}
    for l in open(filename):
        tokens = l.strip().split()
        device = tokens[0][:-1]
        output = tokens[1:]
        G[device] = output
    return G


def reverse(G):
    H = defaultdict(list)
    for s, dd in G.items():
        for d in dd:
            assert s not in H[d]
            H[d].append(s)
    return H

def save_dot(f, g):
    print("digraph G {", file=f)
    for u, vv in g.items():
        print('dac [color="red"];', file=f)
        print('fft [color="red"];', file=f)
        for v in vv:
            print(f"{u} -> {v};", file=f)
    print("}", file=f)


def find_paths_2(G, start, goal):
    paths = []
    Q = [[start]]
    while Q:
        u = Q.pop(0)
        ulast = u[-1]
        if ulast == goal:
            paths.append(u)
            continue
        if ulast != "out":
            for unext in G[ulast]:
                v = u + [unext]
                Q += [v]
    return paths


def find_path_count(G, start, goal):
    count = 0
    Q = deque([start])
    while Q:
        u = Q.popleft()
        if u == goal:
            count += 1
            continue
        if u != "out":
            vv = G[u]
            for v in vv:
                if v != start:
                    Q.appendleft(v)
    return count


def find_path_count_2(G, start, goals):
    goals = set(goals)
    count = 0
    Q = deque([start])
    while Q:
        u = Q.popleft()
        if u in goals:
            count += 1
            continue
        if u != "out":
            vv = G[u]
            for v in vv:
                if v != start:
                    Q.appendleft(v)
    return count


def find_path_count_3(G, start, goal, avoid):
    avoid = set(avoid)
    count = 0
    Q = deque([start])
    while Q:
        u = Q.popleft()
        if u == goal:
            count += 1
            continue
        if u in avoid:
            continue
        if u != "out":
            vv = G[u]
            for v in vv:
                if v != start:
                    Q.appendleft(v)
    return count


def main(filename):
    G = read(filename)
    H = reverse(G)
    #print(G)
    #print(H)

    """
    with open("G.dot", "w") as f:
        save_dot(f, G)
    """

    graph = G

    gate1 = ["tfc", "mjo", "sjg", "ocr", "lbd"]
    gate2 = ["dde", "kda", "ntk"]
    gate3 = ["pes", "emy", "iim"]
    gate4 = ["gyb", "lhg", "ndh", "lmp", "yfw"]
    gate5 = ["hbn", "fsq", "dpt", "ysr", "you"]

    count = find_path_count_3(graph, "svr", "fft", gate2)
    print(f"svr -> fft: {count}")

    C = defaultdict(dict)

    start = "svr"
    for goal in gate1:
        avoid = gate2
        count = find_path_count_3(graph, start, goal, avoid)
        C[start][goal] = count
        print(f"{start} -> {goal} : {count}")

    goal = "fft"
    for start in gate1:
        avoid = gate2
        count = find_path_count_3(graph, start, goal, avoid)
        C[start][goal] = count
        print(f"{start} -> {goal} : {count}")

    start = "fft"
    for goal in gate2:
        avoid = set(gate2)
        avoid.remove(goal)
        count = find_path_count_3(graph, start, goal, avoid)
        C[start][goal] = count
        print(f"{start} -> {goal} : {count}")

    for start in gate2:
        for goal in gate3:
            avoid = set(gate3)
            avoid.remove(goal)
            count = find_path_count_3(graph, start, goal, avoid)
            C[start][goal] = count
            print(f"{start} -> {goal} : {count}")

    for start in gate3:
        for goal in gate4:
            avoid = set(gate4)
            avoid.remove(goal)
            count = find_path_count_3(graph, start, goal, avoid)
            C[start][goal] = count
            print(f"{start} -> {goal} : {count}")

    goal = "dac"
    for start in gate4:
        avoid = gate5
        count = find_path_count_3(graph, start, goal, avoid)
        C[start][goal] = count
        print(f"{start} -> {goal} : {count}")

    start = "dac"
    for goal in gate5:
        avoid = set(gate5)
        avoid.remove(goal)
        count = find_path_count_3(graph, start, goal, avoid)
        C[start][goal] = count
        print(f"{start} -> {goal} : {count}")

    goal = "out"
    for start in gate5:
        avoid = []
        count = find_path_count_3(graph, start, goal, avoid)
        C[start][goal] = count
        print(f"{start} -> {goal} : {count}")

    print(f"{C=}")

    paths = []
    Q = deque([["svr"]])
    while Q:
        u = Q.popleft()
        ulast = u[-1]
        if ulast == "out":
            paths.append(u)
            continue
        for v in C[ulast].keys():
            Q.appendleft(u + [v])

    total = 0
    for path in paths:
        count = 1
        for u, v in zip(path[:-1], path[1:]):
            count *= C[u][v]
        total += count
        print(f"{count=},{path}")
    print(f"{total=}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("input", nargs="?", default="input.txt")
    args = parser.parse_args()
    main(args.input)
