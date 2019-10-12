# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 14:46:34 2019

@author: cw020
"""

# 과제 3


import imageio
from skimage import io
import matplotlib.pyplot as plt
import numpy as np

photo_data = io.imread('sd-3layers.jpg')
photo_data.shape
radius = 3725 / 2
x, y = np.mgrid[0:3725, 0:4797]
circle = ((radius - x)**2 + (4797/2 - y)**2)**0.5 > radius
photo_data[circle] = 255

black_white = np.logical_and(circle, x >= 1862 )
photo_data[black_white] = 0

plt.imshow(photo_data)