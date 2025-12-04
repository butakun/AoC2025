import numpy as np

def main(filename):
    grid = [ [False, *[i == "@" for i in l.strip()], False] for l in open(filename) ]
    jdim = len(grid[0])
    grid.insert(0, [False] * jdim)
    grid.append([False] * jdim)
    grid = np.array(grid)
    print(grid)

    idim, jdim = grid.shape
    sum = 0
    for i in range(1, idim-1):
        for j in range(1, jdim-1):
            if not grid[i, j]:
                continue
            nei = grid[i-1:i+2, j-1:j+2]
            rolls = nei.sum() - 1
            if rolls < 4:
                print(i, j, nei.sum())
                sum += 1

    print(sum)


if __name__ == "__main__":
    main("input.txt")
