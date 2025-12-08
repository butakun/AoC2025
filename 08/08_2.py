import numpy as np
from collections import defaultdict


def read(inputfile):
    junctions = [ [ int(v) for v in l.strip().split(",") ] for l in open(inputfile) ]
    return np.array(junctions)


def main(filename):
    J = read(filename)
    print(J)
    for i, j in enumerate(J):
        print(f"{i}: {j}")

    N = len(J)

    D = []
    for i in range(N):
        for j in range(i + 1, N):
            d = J[i] - J[j]
            d = int((d * d).sum())
            D.append((d, i, j))

    D = sorted(D)
    print(D)

    print("connecting")
    G = defaultdict(set)
    circuits = { i: set([i]) for i in range(N) }
    for d, i, j in D:
        print(f"{i}:{J[i]} - {j}:{J[j]} = {d}")
        G[i].add(j)
        G[j].add(i)

        ci = circuits[i]
        cj = circuits[j]
        if id(ci) == id(cj):
            continue

        circuit = ci | cj
        nodes = circuit.copy()
        while nodes:
            u = nodes.pop()
            circuit.add(u)
            for v in G[u]:
                if v not in circuit:
                    nodes.add(v)
        circuits[i] = circuit
        circuits[j] = circuit

        if len(circuit) == N:
            print(f"COMPLETED: {i}: {J[i]} - {j}: {J[j]}, circuit size = {len(circuit)}")
            print(f"Xi * Xj = {J[i][0] * J[j][0]}")
            break


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("input", nargs="?", default="input.txt")
    args = parser.parse_args()
    main(args.input)
