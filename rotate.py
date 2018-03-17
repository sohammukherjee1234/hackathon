#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 11:27:29 2018

@author: soham
"""

import os

from PIL import Image

from scipy.misc import imsave,imshow,imread

import numpy as np

path="/home/soham/Documents/Deep Learning/hackathon/train_/8"
imagefiles=os.listdir(path)

for image in imagefiles:
    first,extension=image.split('.')
    print "processing "+image
    finalpath=path+"/"+image
    
    pic=imread(finalpath)
 
    rotatedpic=np.flip(pic,1)
    rotate=Image.fromarray(rotatedpic,"L")
    rotate.save(path+"/"+first+"1."+extension)

