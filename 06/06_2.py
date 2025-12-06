import numpy as np


def conv(prob):
    op = str(prob[0][-1])
    vv = np.array(prob)[:, :-1].tolist()
    vv = [ int("".join(v)) for v in vv]
    vv = np.array(vv)
    return vv, op


def read(filename):
    lines = [ list(l.strip("\n")) for l in open(filename) ]
    cols = np.array(lines).T.tolist()

    probs = []
    prob = []
    for col in cols:
        col = np.array(col)
        if np.all(col == " "):
            assert prob
            probs.append(conv(prob))
            prob = []
        else:
            prob.append(col)
    probs.append(conv(prob))
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
