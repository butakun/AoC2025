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


def main(filename):
    ranges, ingredients = read(filename)

    ranges.sort(key=lambda r: r[0])
    print(ranges)

    new_ranges = []
    for i, range_ in enumerate(ranges):
        print(f"*** {i=}, {range_=}, {new_ranges=}")
        if not new_ranges:
            new_ranges.append(range_)
            continue
        range_last = new_ranges.pop()
        if range_[0] <= range_last[1]:
            new_range_last = (range_last[0], max(range_[1], range_last[1]))
            print(f"{range_=}, {range_last=}, {new_range_last=}")
            new_ranges.append(new_range_last)
        else:
            new_ranges.append(range_last)
            new_ranges.append(range_)

    print(f"=== {new_ranges=}")

    count = 0
    for r in new_ranges:
        count += r[1] - r[0] + 1
    print(f"{count=}")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("input", nargs="?", default="input_debug.txt")
    args = parser.parse_args()
    main(args.input)
