import numpy as np

def main(filename):
    grid_ = np.array([ [int(i == "@") for i in l.strip()] for l in open(filename) ])
    grid = np.zeros((grid_.shape[0] + 2, grid_.shape[1] + 2), grid_.dtype)
    grid[1:-1, 1:-1] = grid_
    print(grid)

    r = \
            grid[ :-2,:-2] + grid[ :-2,1:-1] + grid[ :-2,2:] + \
            grid[1:-1,:-2] +                   grid[1:-1,2:] + \
            grid[2:  ,:-2] + grid[2:  ,1:-1] + grid[2:  ,2:]
    print(r)
    nei = r < 4
    rol = grid[1:-1,1:-1] == 1
    can = nei & rol
    rolls = can.sum()
    print(nei)
    print(rol)
    print(can)
    print(rolls)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("input", nargs="?", default="input_debug.txt")
    args = parser.parse_args()
    main(args.input)
