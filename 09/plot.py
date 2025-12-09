import numpy as np
import math
import cv2


def read(filename):
    tiles = [[int(v) for v in l.strip().split(",")] for l in open(filename)]
    return np.array(tiles)


def main(filename):
    tiles = read(filename)
    xmin, ymin = tiles.min(axis=0)
    xmax, ymax = tiles.max(axis=0)
    w = xmax - xmin + 1
    h = ymax - ymin + 1
    ym = (ymax + ymin) // 2
    xm = (xmax + xmin) // 2

    check = []
    for x, y in tiles:
        if abs(y - ym) > 0.05 * h:
            continue
        if x < (xmax - 0.05 * w):
            continue
        if (xmax - 0.01 * w) < x:
            continue
        print(f"check {x}, {y}, {abs(y-ym)=}")
        check.append((x, y))

    xdim = xmax + 1
    ydim = ymax + 1
    G = np.zeros((xdim, ydim, 3), np.uint8)

    np.save(open("poly.npy", "wb"), tiles)
    print(f"{xmin=}, {xmax=}, {ymin=}, {ymax=}")

    pts = np.array([[tiles.astype(np.int32).copy()]])
    cv2.fillPoly(G, pts, (255, 255, 255))

    for x, y in tiles:
        cv2.circle(G, (x, y), 200, (0,255,255), -1)

    for x, y in check:
        cv2.circle(G, (x, y), 300, (0,0,255), -1)
    cv2.circle(G, (94671, 50270), 300, (255,0,0), -1)
    cv2.circle(G, (94671, 48487), 300, (255,0,0), -1)


    G = cv2.resize(G, None, fx=0.01, fy=0.01)
    cv2.imwrite("map.png", G)


main("./input.txt")
