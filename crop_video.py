# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 19:55:30 2018

Just a script to crop a video, since google did not help with that.

@author: Arsku
"""

import numpy as np
import cv2

INPUT_FILENAME = 'cat.mp4'
OUTPUT_FILENAME = 'cropped_cat.mp4'
SCALE_FACTOR = 0.5
OFFSETX = -50
OFFSETY = -50
WIDTH = 384
HEIGHT = 128

cap = cv2.VideoCapture(INPUT_FILENAME)

fourcc = cv2.VideoWriter_fourcc(*'MPEG')
out = cv2.VideoWriter(OUTPUT_FILENAME,fourcc, 20.0, (WIDTH,HEIGHT))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.resize(frame,(0,0), fx=SCALE_FACTOR, fy=SCALE_FACTOR, interpolation = cv2.INTER_CUBIC)
        
        M = np.float32([[1,0,OFFSETX],[0,1,OFFSETY]])
        dst = cv2.warpAffine(frame,M,(WIDTH,HEIGHT))
        
        out.write(dst)
    

    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
