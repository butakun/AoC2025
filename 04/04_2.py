import numpy as np

def read(filename):
    grid_ = np.array([ [int(i == "@") for i in l.strip()] for l in open(filename) ])
    grid = np.zeros((grid_.shape[0] + 2, grid_.shape[1] + 2), grid_.dtype)
    grid[1:-1, 1:-1] = grid_
    return grid


def clean(grid):
    r = \
            grid[ :-2,:-2] + grid[ :-2,1:-1] + grid[ :-2,2:] + \
            grid[1:-1,:-2] +                   grid[1:-1,2:] + \
            grid[2:  ,:-2] + grid[2:  ,1:-1] + grid[2:  ,2:]
    nei = r < 4
    rol = grid[1:-1,1:-1] == 1
    can = nei & rol
    grid[1:-1,1:-1][can] = 0
    rolls = can.sum()
    return rolls


def main(filename):
    grid = read(filename)
    rolls0 = grid.sum()
    print(grid)
    print(rolls0)

    while clean(grid) > 0:
        pass

    rolls = grid.sum()
    print(rolls, rolls0 - rolls)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("input", nargs="?", default="input_debug.txt")
    args = parser.parse_args()
    main(args.input)
