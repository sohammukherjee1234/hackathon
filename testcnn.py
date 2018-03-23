#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 22:42:11 2018

@author: soham
"""

import torch.nn as nn
import torch
import torch.nn.functional as F
import torch.optim as optim
import torchvision.datasets as dt
import torchvision.transforms as transforms
import torchvision.datasets as datasets
import torchvision.utils as utils
from torch.utils.data import DataLoader
from torch.autograd import Variable
import numpy as np
import matplotlib.pyplot as pl
import torchvision.models as models
from scipy.misc import imread
import os
import os.path
from scipy.misc import imsave
from scipy.misc import imread
import matplotlib.pyplot as plt

transform = transforms.Compose([
            transforms.Scale((224,224)),
            transforms.ToTensor(),
            transforms.Normalize(mean = [ 0.485, 0.456, 0.406 ],
                                std = [ 0.229, 0.224, 0.225 ]),
])

net=torch.load('model.pth')
path="/media/nibaran/codes/Soham/githubrepo/hackathon/excess"

test_data=datasets.ImageFolder(path, transform)

test_loader=DataLoader(test_data,batch_size=1,num_workers=1)


for batch in test_loader:
    inputs,_=batch
    inputs=Variable(inputs)
    outputs=net(inputs)
    _, predicted = torch.max(outputs.data, 1)
    print(predicted)
