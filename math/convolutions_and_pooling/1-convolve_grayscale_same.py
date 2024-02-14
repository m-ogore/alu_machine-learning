#!/usr/bin/env python3

'''
    def convolve_grayscale_same(images, kernel): that performs a same convolution on grayscale images:

        images is a numpy.ndarray with shape (m, h, w) containing multiple grayscale images
        m is the number of images
        h is the height in pixels of the images
        w is the width in pixels of the images
        kernel is a numpy.ndarray with shape (kh, kw) containing the kernel for the convolution
        kh is the height of the kernel
        kw is the width of the kernel
        if necessary, the image should be padded with 0’s
        You are only allowed to use two for loops; any other loops of any kind are not allowed
        Returns: a numpy.ndarray containing the convolved images

'''
import numpy as np
def convolve_grayscale_same(images, kernel):
    m,w,h = images.shape

    kh,kw = kernel.shape
    # how to zero pad with numpy https://stackoverflow.com/questions/38191855/zero-pad-numpy-array

    top, left = 0, 0

    if w%kw != 0:
        
        #((top, bottom), (left, right)):
        top = w%kw
        
    if h%kh != 0:
        left = h%kh
    
    bottom = top
    right = left

    images = np.pad(images, ((0, 0), (top,bottom),(left,right)), 'constant')

    print(images.shape)
    

    
    convolved_image = np.zeros((m,images.shape[1]//kw, images.shape[2]//kh))
    print(convolved_image)


    for image in images:
        for i in range(h-kh+1):
            for j in range(w-kw+1):
                image_region = image[i:i+kh, j:j+kw]
                conv_el = np.sum(image_region*kernel)
                    
            convolved_image[j].append(conv_el)
    return np.array(convolved_image)








#images = np.array([[[1,2,4,5],[3,4,4,5], [1,2,4,5],[3,4,4,5]]])
images = images = np.ones((1, 4, 6)) 
kernel = np.array([[1 ,0, -1], [1, 0, -1], [1, 0, -1]])
print(images)
convolve_grayscale_same(images, kernel)