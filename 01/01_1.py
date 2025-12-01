def main(filename):
    lists = [(l[0], int(l[1:])) for l in open(filename)]
    print(lists)

    i = 50
    hits = 0
    for d, di in lists:
        if d == "L":
            di = -di
        i += di
        if i < 0:
            i = 100 - abs(i) % 100
        if i > 99:
            i = i % 100
        if i == 0:
            hits += 1
        print(f"{d=}, {di=}, {i=}, {hits=}")


if __name__ == "__main__":
    main("input.txt")
