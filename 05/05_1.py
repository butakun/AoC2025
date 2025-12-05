import numpy as np

def read(filename):
    ranges = []
    f = open(filename)
    for l in f:
        if not (l := l.strip()):
            break
        i0, i1 = map(int, l.split("-"))
        ranges.append((i0, i1))

    ingredients = [int(l) for l in f]
    return ranges, ingredients


def is_fresh(i, rr):
    for r in rr:
        if r[0] <= i and i <= r[1]:
            return True
    return False

def main(filename):
    ranges, ingredients = read(filename)

    f = 0
    for i in ingredients:
        if (fresh := is_fresh(i, ranges)):
            f += 1
        print(f"{i} -> {fresh}")
    print(f)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("input", nargs="?", default="input_debug.txt")
    args = parser.parse_args()
    main(args.input)
