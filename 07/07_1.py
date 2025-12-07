import numpy as np

def read(filename):
    grid = [ list(l.strip()) for l in open(filename) ]
    return np.array(grid)


def cast(grid, beams):
    idim, jdim = grid.shape

    i, j = beams.pop(0)

    if i >= (idim - 1):
        return []

    isp = np.where(grid[i+1:,j] == "^")
    if len(isp[0]) == 0:
        print(f"({i},{j}) ----> ({idim-1},{j})")
        grid[i+1:, j] = "|"
        return []

    isp = i + 1 + int(isp[0][0])

    print(f"({i},{j}) -> ({isp},{j})")
    assert grid[i, j] == "|"

    grid[i:isp, j] = "|"

    new_beams = []
    if j > 0 and grid[isp, j-1] == ".":
        new_beams.append((isp, j-1))
        grid[isp, j-1] = "|"
    if j < (jdim - 1) and grid[isp, j+1] == ".":
        new_beams.append((isp, j+1))
        grid[isp, j+1] = "|"
    return new_beams


def dump(grid):
    for l in grid:
        print("".join(l))


def main(filename):
    grid = read(filename)
    dump(grid)

    b = np.where(grid == "S")
    b = (int(b[0][0]), int(b[1][0]))
    grid[b[0], b[1]] = "|"
    beams = [b]
    print(beams)

    while beams:
        print("------")
        new_beams = cast(grid, beams)
        if new_beams:
            print(f"{new_beams=}")
        beams += new_beams
    dump(grid)

    ssi, ssj = np.where(grid == "^")
    ss = list(zip(ssi, ssj))
    count = 0
    for si, sj in ss:
        si, sj = int(si), int(sj)
        if grid[si-1, sj] == "|":
            count += 1
            print(count, si, sj)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("input", nargs="?", default="input_debug.txt")
    args = parser.parse_args()
    main(args.input)
