import numpy as np
from collections import defaultdict


def read(inputfile):
    junctions = [ [ int(v) for v in l.strip().split(",") ] for l in open(inputfile) ]
    return np.array(junctions)


def main(filename, connect):
    J = read(filename)
    print(J)
    for i, j in enumerate(J):
        print(f"{i}: {j}")

    N = len(J)

    D = []
    for i in range(N):
        for j in range(i + 1, N):
            d = float(np.linalg.norm(J[i] - J[j]))
            D.append((d, i, j))

    D = sorted(D)
    print(D)

    print("shortest:")
    G = defaultdict(set)
    for d, i, j in D[:connect]:
        print(f"{J[i]} - {J[j]}")
        G[i].add(j)
        G[j].add(i)
    print(G)

    nodes = set(range(N))

    circuits = []
    while nodes:
        u = nodes.pop()
        circuit = [u]
        vv = [u]
        while vv:
            v = vv.pop(0)
            w = G[v]
            for node in w:
                if node not in circuit:
                    circuit.append(node)
                    vv.append(node)
                    nodes.remove(node)
                    print(f"{node=},{circuit=},{vv=},{nodes=}")
        circuits.append(circuit)

    circuits.sort(key=lambda c: len(c), reverse=True)
    print(circuits)

    sizes = [ len(c) for c in circuits ]
    print(sizes)

    res = 1
    for v in sizes[:3]:
        res *= v
    print(res)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("input", nargs="?", default="input.txt")
    args = parser.parse_args()
    if args.input == "input_debug.txt":
        connect = 10
    else:
        connect = 1000
    main(args.input, connect)
