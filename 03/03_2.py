def joltage(bank):

    L = len(bank)
    vv = []
    i = 0

    while (l := len(vv)) < 12:
        m = L - (12 - l - 1)
        v = max(bank[i:m])
        vv.append(v)
        i = i + bank[i:m].index(v) + 1

    return sum([pow(10, 12 - i - 1) * v for i, v in enumerate(vv)])


def main(filename):
    banks = [ [ int(i) for i in l.strip() ] for l in open(filename) ]

    sum = 0
    for bank in banks:
        j = joltage(bank)
        print("".join(map(str, bank)), j)
        sum += j
    print(f"{sum=}")


if __name__ == "__main__":
    main("input.txt")
