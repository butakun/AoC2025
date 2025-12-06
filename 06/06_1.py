import numpy as np


def read(filename):
    lines = [ l.strip().split() for l in open(filename) ]
    trans = np.array(lines).T.tolist()
    probs = []
    for t in trans:
        vv = np.array([int(v) for v in t[:-1]])
        op = t[-1]
        probs.append((vv, op))

    return probs

def main(filename):
    probs = read(filename)
    print(probs)

    res = 0
    for vv, op in probs:
        if op == "+":
            answer = vv.sum()
        else:
            answer = vv.prod()
        print(vv, op, answer)
        res += answer
    print(res)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("input", nargs="?", default="input_debug.txt")
    args = parser.parse_args()
    main(args.input)
