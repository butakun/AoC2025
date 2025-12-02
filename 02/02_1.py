def is_invalid_(x):

    l = len(x)
    for i in range(1, l // 2 + 1):
        dx = x[:i]
        m = l // i
        xx = dx * m
        if x == xx:
            print(f"{x=}, {l=},{i=},{dx=},{m=},{xx=}")
            return True
    return False


def is_invalid(x):

    l = len(x)
    if l % 2 != 0:
        return False

    dl = l // 2
    xx = x[:dl] * 2
    if x == xx:
        print(f"{x=}, {l=}, {dl=}, {xx=}")
    return x == xx


def main(filename):
    ranges = [ [ int(i) for i in pair.split("-")] for pair in open(filename).readline().strip().split(",") ]

    xsum = 0
    for x1, x2 in ranges:
        invalids = 0
        for x in range(x1, x2+1):
            if is_invalid(str(x)):
                invalids += 1
                xsum += x
    print(f"{xsum=}")


if __name__ == "__main__":
    main("input.txt")
