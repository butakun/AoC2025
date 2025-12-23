import numpy as np
from collections import defaultdict, deque


def read(filename):
    f = open(filename)
    shapes = []
    for _ in range(6):
        i = int(f.readline().strip()[:-1])
        shape = np.array([[v == "#" for v in f.readline().strip()] for _ in range(3)])
        shapes.append(shape)
        f.readline()

    regions = []
    for l in f:
        tokens = l.strip().split()
        w, h = tokens[0][:-1].split("x")
        w, h = int(w), int(h)
        presents = [int(i) for i in tokens[1:]]
        regions.append((w, h, presents))

    return shapes, regions


def dump(s):
    for l in s:
        print("".join(["#" if b else "." for b in l]))


def shapebit(s):
    return sum([1 << i if b else 0 for i, b in enumerate(s.reshape(9))])


def can_fit_bit(rbit, sbit):
    raise NotImplementedError
    return ((rbit | sbit) & sbit) == 0


def can_fit(r, s):
    return np.all(~(r & s))


def place_bits(region, shape, i, j):
    area = region[i:i+3, j:j+3]
    abit = shapebit(area)
    sbit = shapebit(shape)
    if can_fit(abit, sbit):
        rnew = region.copy()
        rnew[i:i+3, j:j+3] = shape
        return rnew
    return None


def place(region, shape, i, j):
    area = region[i:i+3, j:j+3]
    print("--")
    print("placing")
    dump(shape)
    print("onto")
    dump(area)
    print("--")
    if can_fit(area, shape):
        area |= shape
        return True
    return False


def rotate_and_place(region, shape):
    h, w = region.shape
    print("Trying to place this shape")
    dump(shape)
    for i in range(h - 2):
        for j in range(w - 2):
            print(f"trying {i=}, {j=}")
            placed = place(region, shape, i, j)
            if placed:
                return True
    return False


def main(filename):
    shapes, regions = read(filename)

    for i, shape in enumerate(shapes):
        print(i, shape.sum())


    count = 0
    for w, h, presents in regions:
        p = sum([shapes[i].sum() * n for i, n in enumerate(presents)])
        if p <= w * h:
            count += 1
        print(f"region: {w * h =}, {p=}, {(p <= w*h)=}")
    print(count)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("input", nargs="?", default="input.txt")
    args = parser.parse_args()
    main(args.input)
