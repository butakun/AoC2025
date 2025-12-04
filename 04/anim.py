p = __import__("04_2")


def dump(i, grid):
    G = grid[1:-1, 1:-1]
    img = np.zeros((G.shape[1], G.shape[0], 3), np.uint8)
    #img[:, :, :] = [100, 100, 100]
    img[G == True] = [255, 255, 255]
    cv2.imwrite(f"image.{i:04d}.png", img)


def main(filename):
    grid = p.read(filename)
    print(grid)

    i = 0
    dump(i, grid)
    while p.clean(grid) > 0:
        i += 1
        dump(i, grid)


if __name__ == "__main__":
    main("input.txt")
