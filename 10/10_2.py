import numpy as np
import scipy


def read(filename):
    machines = []
    def wiring_to_array(w, n):
        #a = np.zeros(n, np.int64)
        a = [0] * n
        for i in w:
            a[i] = 1
        return a

    for l in open(filename):
        tokens = l.strip().split(" ")
        buttons_, joltages_ = tokens[1:-1], tokens[-1]

        #joltages = np.array([int(v) for v in joltages_[1:-1].split(",")])
        joltages = [int(v) for v in joltages_[1:-1].split(",")]
        n = len(joltages)

        #buttons = np.array([wiring_to_array([int(v) for v in b[1:-1].split(",")], n) for b in buttons_])
        buttons = [wiring_to_array([int(v) for v in b[1:-1].split(",")], n) for b in buttons_]

        print(f"{buttons_=}, {joltages_=} {buttons=}, {joltages=}")
        machines.append((buttons, joltages))
    return machines


def solve(buttons, joltages):

    nb = len(buttons)
    nj = len(joltages)

    A = np.vstack(buttons).T
    #print("A")
    #print(A)

    b = np.array(joltages, A.dtype)
    #print("b")
    #print(b)

    c = np.ones(nb, A.dtype)
    #print("c")
    #print(c)

    bounds = [(0, None) for i in range(nb)]
    res = scipy.optimize.linprog(c=c, A_eq=A, b_eq=b, bounds=bounds, integrality=1)
    print(res)
    x = res.x.astype(int)
    print(f"  {x=}")
    return int(res.fun)


def main(filename):
    machines = read(filename)
    print(machines)

    sum = 0
    for buttons, joltages in machines:
        print(f"MACHINE {buttons}, {joltages}")
        count = solve(buttons, joltages)
        print(f"  {count=}")
        sum += count
        print()
    print(f"{sum=}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("input", nargs="?", default="input.txt")
    args = parser.parse_args()
    main(args.input)
