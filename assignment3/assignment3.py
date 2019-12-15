# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 14:46:34 2019

@author: cw020
"""

# 과제 3

from skimage import io
import matplotlib.pyplot as plt
import numpy as np

photo_data = io.imread('sd-3layers.jpg') # 이미지 읽기
photo_data.shape # 이미지 크기 확인
radius = 3725 / 2 # 반지름 변수
x, y = np.mgrid[0:3725, 0:4797] # 좌표 계산을 위해 만듦
circle = ((radius - x)**2 + (4797/2 - y)**2)**0.5 > radius # 반지름 보다 거리가 멀면 원 밖

photo_data[circle] = 255 #  원 밖 전부 흰색으로 만들기

plt.imshow(photo_data)

black_white = np.logical_and(circle, x >= 1862 ) # 원 밖이면서 x 절반 아래
photo_data[black_white] = 0 # 원 밖이면서 절반 아래를 검정색으로

plt.imshow(photo_data) # 이미지 출력