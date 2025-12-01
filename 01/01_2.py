def main(filename):
    lists = [(l[0], int(l[1:])) for l in open(filename)]
    print(lists)

    i = 50
    hits = 0
    for d, di in lists:
        i0 = i
        if d == "R":
            if di > 100:
                hits += di // 100
            i += di % 100
            if i > 100:
                hits += 1
        elif d == "L":
            if di > 100:
                hits += di // 100
            i -= di % 100
            if i0 > 0 and i < 0:
                hits += 1
        i = i % 100
        if i == 0:
            hits += 1
        print(f"{d=}, {di=}, {i0=}, {i=}, {hits=}")


if __name__ == "__main__":
    main("input.txt")
