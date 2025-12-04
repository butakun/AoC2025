import numpy as np

def clean(grid):
    idim, jdim = grid.shape

    indices = []
    for i in range(1, idim-1):
        for j in range(1, jdim-1):
            if not grid[i, j]:
                continue
            nei = grid[i-1:i+2, j-1:j+2]
            rolls = nei.sum() - 1
            if rolls < 4:
                indices.append((i, j))

    for i, j in indices:
        grid[i, j] = False

    return len(indices)


def main(filename):
    grid = [ [False, *[i == "@" for i in l.strip()], False] for l in open(filename) ]
    jdim = len(grid[0])
    grid.insert(0, [False] * jdim)
    grid.append([False] * jdim)
    grid = np.array(grid)
    rolls0 = grid.sum()
    print(grid)
    print(rolls0)

    while clean(grid) > 0:
        pass

    rolls = grid.sum()
    print(rolls, rolls0 - rolls)

if __name__ == "__main__":
    main("input.txt")
