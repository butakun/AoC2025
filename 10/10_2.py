import numpy as np
import math
from collections import defaultdict
from priority_queue import PriorityQueue


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


def list_active_buttons(buttons, joltages):
    active_buttons = [None] * len(joltages)
    for i, joltage in enumerate(joltages):
        bb = []
        if joltage > 0:
            for ib, button in enumerate(buttons):
                if button[i] > 0:
                    bb += [ib]
        active_buttons[i] = [int(joltage), bb]
    return active_buttons


def button_combo(buttons, joltage, active_button_indices):
    n = len(buttons)
    m = len(active_button_indices)
    C = []
    Q = [[i, i] for i in range(joltage + 1)]
    while Q:
        u = Q.pop(0)
        s, b = u[0], u[1:]
        if s == joltage:
            while len(b) < m:
                b.append(0)
            C.append(b)
            continue
        if len(b) == m:
            continue
        for db in range(joltage - s + 1):
            v = b + [db]
            v = [s + db, *v]
            Q.append(v)

    # from active button indices to button indices
    CC = []
    for c in C:
        cc = [None] * n
        for iab, coef in zip(active_button_indices, c):
            cc[iab] = coef
        CC.append(cc)
    return CC


def merge_button_coefs(coefs1, coefs2):
    merged = coefs1.copy()
    for i, (c1, c2) in enumerate(zip(coefs1, coefs2)):
        if c1 is None:
            merged[i] = c2
        else:
            if c2 is not None and c1 != c2:
                # cannot merged, conflicting pair of coefficients
                return None
    return merged


def solve(buttons, joltages):
    active_buttons = list_active_buttons(buttons, joltages)
    #print(f"  {active_buttons=}")

    nb = len(buttons)
    candidates = [[None] * nb]
    for i, joltage in enumerate(joltages):
        print(f"  {i=}, {joltage=}")
        _, active_button_indices = active_buttons[i]
        combo = button_combo(buttons, joltage, active_button_indices)
        #print(f"joltage={int(joltage)},{active_button_indices=}")
        #print("generating new candidates")
        new_candidates = []
        for parent in candidates:
            #print(f"  Parent={parent}")
            for coefs in combo:
                child = merge_button_coefs(parent, coefs)
                if child is not None:
                    new_candidates.append(child)
                    #print(f"    {child}")
        candidates = new_candidates

    print("Counting # of button presses")
    min_count = None
    for candidate in candidates:
        count = sum(candidate)
        if min_count is None or count < min_count:
            min_count = count
        print(f"  {candidate} => {sum(candidate)}")
    print(f"  Minimum = {min_count}")
    return min_count


def sort_problem(buttons, joltages):
    n = len(joltages)
    sorted_indices = sorted(zip(joltages, range(n)))
    joltages_sorted = [v for v, _ in sorted_indices]
    indices_sorted = [i for _, i in sorted_indices]

    buttons_sorted = []
    for button in buttons:
        button_sorted = [button[i] for i in indices_sorted]
        buttons_sorted.append(button_sorted)

    return buttons_sorted, joltages_sorted


def main(filename):
    machines = read(filename)
    print(machines)

    sum = 0
    for buttons, joltages in machines:
        buttons_, joltages_ = sort_problem(buttons, joltages)
        print(f"MACHINE {buttons_}, {joltages_}")
        count = solve(buttons_, joltages_)
        sum += count
        print()
    print(f"{sum=}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("input", nargs="?", default="input.txt")
    args = parser.parse_args()
    main(args.input)
