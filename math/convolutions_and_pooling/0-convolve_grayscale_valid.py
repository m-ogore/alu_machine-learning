#!/usr/bin/env python3
import numpy as np

#Create the function to convolve
def convolve_grayscale_valid(images, kernel):
    #get a multidimensional array of m- number of images each with h*w number of elements in it
    m, h, w = images.shape
    #ther hernel isof dimensions of columns kh and rows kw
    kh, kw = kernel.shape
    # the number of strides to be taken vertically will be number of rowsof the image - number of rowsin the kernel
    output_h = h - kh + 1
    # the number of strides to be taken horizontally will be number of columns of the image - number of columnsin the kernel
    output_w = w - kw + 1
    output = np.zeros((m, output_h, output_w))

    for i in range(output_h):
        for j in range(output_w):
            output[:, i, j] = np.sum(images[:, i:i+kh, j:j+kw] * kernel, axis=(1, 2))

    return output

