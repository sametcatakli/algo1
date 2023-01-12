from random import randrange

from umage import *


def grayscale(mat_img):
    res = []
    for row in mat_img:
        res_row = []
        for r, g, b in row:
            res_row.append((int(0.2125 * r + 0.7154 * g + 0.0721 * b),) * 3)
        res.append(res_row)
    return res


def pixel(img, i, j, default):
    height = len(img)
    witdh = len(img[0])
    if 0 <= i < height and 0 <= j < witdh:
        return img[i][j]
    else:
        return default


def normalize(x):
    return min(max(int(round(x)), 0), 255)


def appliquer_convolution(img, kernel, i, j):
    sum_r, sum_g, sum_b = (0, 0, 0)
    for ki in [0, 1, 2]:
        for kj in [0, 1, 2]:
            kv = kernel[ki][kj]
            r, g, b = pixel(img, (i - 1) + ki, (j - 1) + kj, (0, 0, 0))
            sum_r += kv * r
            sum_g += kv * g
            sum_b += kv * b
    return normalize(sum_r), normalize(sum_g), normalize(sum_b)


def convolution_x(mat_img, kernel):
    res = []
    for i in range(len(mat_img)):
        for j in range(len(mat_img[i])):
            res.append(appliquer_convolution(mat_img, kernel, i, j))
    return res


def convolution_y(mat_img, kernel):
    res = []
    for i in range(len(mat_img)):
        for j in range(len(mat_img[i])):
            res.append(appliquer_convolution(mat_img, kernel, j, i))
    return res


def main():
    y = [[-1, -2, -1],
         [0, 0, 0],
         [1, 2, 1]]

    x = [[-1, 0, 1],
         [-2, 0, 2],
         [-1, 0, 1]]
    img = load('shrek.png')
    gray = grayscale(img)
    save(gray, randrange(1, 100), "png")
    contour = convolution_x(gray, x)
    contour2 = convolution_y(gray, y)
    print(contour)
    save(contour2, "sobel", "png")


if __name__ == '__main__':
    main()
