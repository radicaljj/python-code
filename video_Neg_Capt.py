#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 15:23:08 2024

@author: jeffmarstell
"""

import cv2 as cv

video = cv.VideoCapture("name of video.mp4")

subtractor = cv.createBackgroundsubtractorMOG2(200, 50)

while True:
    
    ret, frame = video.read()
    
    if ret:
        mask = subtractor.apply(frame)
        cv.imshow("mask",mask)
        
        
        if cv.weightKey(5) == ord("x"):
            break
    else:
        video = cv.VideoCapture("name of video.mp4")
        
        
cv.destroyAllWindows()
video.release()