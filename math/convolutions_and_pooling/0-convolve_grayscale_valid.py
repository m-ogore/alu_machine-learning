#!/usr/bin/env python3
import numpy as np

'''
    Write a function def convolve_grayscale_valid(images, kernel): that performs a valid convolution on grayscale images:

    images is a numpy.ndarray with shape (m, h, w) containing multiple grayscale images
    m is the number of images
    h is the height in pixels of the images
    w is the width in pixels of the images
    kernel is a numpy.ndarray with shape (kh, kw) containing the kernel for the convolution
    kh is the height of the kernel
    kw is the width of the kernel
    You are only allowed to use two for loops; any other loops of any kind are not allowed
    Returns: a numpy.ndarray containing the convolved images
'''
def convolve_grayscale_valid(images, kernel):
    m =images.shape[0] 
    h = images.shape[1]
    w = images.shape[2]
    
    kh = kernel.shape[0]
    kw = kernel.shape[1]

    convolved_image  = []

    for image in images:
        for i in range(h-kh+1):
            for j in range(w-kw+1):
                image_region = image[i:i+kh, j:j+kw]
                conv_el = np.sum(image_region*kernel)
                    
            convolved_image.append(conv_el)
    return np.array(convolved_image)