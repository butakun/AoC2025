import numpy as np
from collections import defaultdict


def read(filename):
    grid = [ list(l.strip()) for l in open(filename) ]
    return np.array(grid)


def cast(grid, beam):
    idim, jdim = grid.shape

    i, j = beam[-1]

    if i >= (idim - 1):
        return []

    isp = np.where(grid[i+1:,j] == "^")
    if len(isp[0]) == 0:
        # no splitter
        return []

    isp = i + 1 + int(isp[0][0])

    #print(f"({i},{j}) -> ({isp},{j})")
    new_beams = []
    if j > 0 and grid[isp, j-1] == ".":
        new_beams += [beam + [(isp, j-1)]]
    if j < (jdim - 1) and grid[isp, j+1] == ".":
        new_beams += [beam + [(isp, j+1)]]
    return new_beams


def build_dag(grid, s):
    idim, jdim = grid.shape

    dag = defaultdict(set)

    first = grid[s[0]:,s[1]].tolist().index("^")
    dag[s].add((first, s[1]))

    ss = np.where(grid == "^")
    ss = ss[0].tolist(), ss[1].tolist()
    for i, j in zip(*ss):
        if j > 0:
            try:
                isp = grid[i:, j-1].tolist().index("^")
                isp += i
                dag[(i, j)].add((isp, j-1))
            except:
                dag[(i, j)].add((idim, j-1))
        if j < jdim - 1:
            try:
                isp = grid[i:, j+1].tolist().index("^")
                isp += i
                dag[(i, j)].add((isp, j+1))
            except:
                dag[(i, j)].add((idim, j+1))

    dagr = defaultdict(set)
    for u, vv in dag.items():
        for v in vv:
            dagr[v].add(u)

    return dag, dagr


def dump(grid):
    for l in grid:
        print("".join(l))


def main(filename):
    grid = read(filename)
    idim, jdim = grid.shape
    dump(grid)

    s = np.where(grid == "S")
    s = (int(s[0][0]), int(s[1][0]))

    dag, dagr = build_dag(grid, s)
    print(dag)
    print(dagr)

    nodes = {k: 0 for k in dag.keys()}
    for u in dagr.keys():
        if u not in nodes:
            nodes[u] = 0
    nodes[s] = 1

    uu = sorted(nodes.keys(), key=lambda ij: ij[0])
    print(f"{uu=}")

    for u in uu:
        if u in dagr:
            for v in dagr[u]:
                print(f"{u=}, {v=}, +{nodes[v]=}")
                nodes[u] += nodes[v]
    print(nodes)

    count = 0
    for u in nodes:
        if u[0] != idim:
            continue
        count += nodes[u]
        print(f"{u=}, {nodes[u]=}, {count=}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("input", nargs="?", default="input_debug.txt")
    args = parser.parse_args()
    main(args.input)
