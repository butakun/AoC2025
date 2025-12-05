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

    count = 0
    range_last = ranges[0]
    for range_ in ranges[1:]:
        if range_[0] <= range_last[1]:
            range_last = range_last[0], max(range_[1], range_last[1])
        else:
            count += range_last[1] - range_last[0] + 1
            range_last = range_
        print(f"{range_=}, {range_last=}, {count=}")
    count += range_last[1] - range_last[0] + 1
    print(count)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("input", nargs="?", default="input_debug.txt")
    args = parser.parse_args()
    main(args.input)
