#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 15:33:34 2024

@author: jeffmarstell
"""

import cv2 as cv
import numpy as np

camera = cv.videoCapture("video name goes here.mp4")

while True:
    _, frame = camera.read()
    
    cv.imshow('camera', frame)
    
    laplacian = cv.lapacian(frame, cv.CV_64F)
    laplacian = np.uint8(laplacian)
    cv.imshow('laplacian', laplacian)
    
    edges = cv.canny(frame, 100,100)
    cv.imshow('canny', edges)
    
    if cv.waitKey(5) == ord('x'):
        break
    
    
camera.release()
cv.destroyAllWindows()