import numpy as np
import math
from collections import defaultdict


def read(filename):
    tiles = [[int(v) for v in l.strip().split(",")] for l in open(filename)]
    return np.array(tiles)


def intersects(xmin, xmax, ymin, ymax, tiles):
    for x, y in tiles:
        if xmin < x and x < xmax and ymin < y and y < ymax:
            return True
    return False

def main(filename):
    tiles = read(filename)
    N = tiles.shape[0]
    xmin, ymin = tiles.min(axis=0)
    xmax, ymax = tiles.max(axis=0)
    w = xmax - xmin + 1
    h = ymax - ymin + 1
    ym = (ymax + ymin) // 2
    xm = (xmax + xmin) // 2

    check = []
    for x, y in tiles:
        if abs(y - ym) > 0.05 * h:
            continue
        if x < (xmax - 0.05 * w):
            continue
        if (xmax - 0.01 * w) < x:
            continue
        print(f"check {x}, {y}, {abs(y-ym)=}")
        check.append((x, y))

    assert len(check) == 2
    p1 = check[0]
    p2 = check[1]
    if p1[1] > p2[1]:
        tmp = p2
        p2 = p1
        p1 = p2

    amax = None
    x1, y1 = p1
    for p3 in tiles[:N]:
        x3, y3 = p3
        if y1 < y3:
            continue
        xmin = min(x1, x3)
        xmax = max(x1, x3)
        ymin = min(y1, y3)
        ymax = max(y1, y3)

        w = xmax - xmin + 1
        h = ymax - ymin + 1
        a = w * h
        if amax is None or amax < a:
            if not intersects(xmin, xmax, ymin, ymax, tiles):
                amax = a
                print(f"{p1=}, {p3=}, amax={int(amax)}")

    x1, y1 = p2
    for p3 in tiles[:N]:
        x3, y3 = p3
        if y3 < y1:
            continue
        xmin = min(x1, x3)
        xmax = max(x1, x3)
        ymin = min(y1, y3)
        ymax = max(y1, y3)

        w = xmax - xmin + 1
        h = ymax - ymin + 1
        a = w * h
        if amax is None or amax < a:
            if not intersects(xmin, xmax, ymin, ymax, tiles):
                amax = a
                print(f"{p2=}, {p3=}, amax={int(amax)}")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("input", nargs="?", default="input.txt")
    args = parser.parse_args()
    main(args.input)
