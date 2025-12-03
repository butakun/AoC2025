def joltage(bank):

    v1 = max(bank[:-1])
    i1 = bank.index(v1)
    v2 = max(bank[i1+1:])
    return v1 * 10 + v2


def main(filename):
    banks = [ [ int(i) for i in l.strip() ] for l in open(filename) ]

    sum = 0
    for bank in banks:
        j = joltage(bank)
        print("".join(map(str, bank)), j)
        sum += j
    print(sum)


if __name__ == "__main__":
    main("input.txt")
