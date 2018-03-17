#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 11:58:30 2018

@author: soham
"""

import os

num=100

path="/home/soham/Documents/Deep Learning/hackathon/train_/"

for i in range(14):
    currpath=path+str(i)
    movepath=path+"train/"+str(i)
    images=os.listdir(currpath)
    if os.path.isdir(movepath)==False:
        os.makedirs(movepath)
    
    itr=0
    for im in images:
        os.rename(currpath+"/"+im,movepath+"/"+im)
        itr+=1
        if itr==100:
            break