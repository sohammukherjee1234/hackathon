#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 22:20:01 2018

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



# LOADERS
transform = transforms.Compose([
            transforms.Scale((224,224)),
            transforms.ToTensor(),
            transforms.Normalize(mean = [ 0.485, 0.456, 0.406 ],
                                std = [ 0.229, 0.224, 0.225 ]),
])
train_path="/media/nibaran/codes/Soham/hackathon dataset/train_/train"
val_path="/media/nibaran/codes/Soham/hackathon dataset/train_/val"

train_data=datasets.ImageFolder(train_path,transform)
val_data=datasets.ImageFolder(val_path,transform)

train_loader=DataLoader(train_data,batch_size=4,shuffle=True,num_workers=1)
val_loader=DataLoader(val_data,batch_size=4,shuffle=True,num_workers=1)


        

net=models.resnet18(pretrained=False)
net.fc=nn.Linear(512,14)

criterion=nn.NLLLoss(size_average=True)
learn_rate=0.1
optimizer=optim.Adam(net.parameters())
net=net.cuda()
train_loss_vs_epoch=[]
val_loss_vs_epoch=[]

for epoch in range(20):
    print("running epoch "+str(epoch))
    train_loss=0.0
    val_loss=0.0
    for batch in train_loader:
        net=net.train(True)
        inputs,labels=batch
        inputs,labels=Variable(inputs),Variable(labels)
        inputs,labels=inputs.cuda(),labels.cuda()
        optimizer.zero_grad()
        outputs=net(inputs)
        loss=criterion(F.log_softmax(outputs),labels)
        _,predicted=torch.max(outputs.data,1)
        loss.backward()
        optimizer.step()
        train_loss+=loss.data[0]
    
    train_loss_vs_epoch.append(train_loss/len(train_loader))
    
    for batch in val_loader:
        net=net.train(False)
        inputs,labels=batch
        inputs,labels=Variable(inputs),Variable(labels)
        inputs,labels=inputs.cuda(),labels.cuda()
        outputs=net(inputs)
        loss=criterion(F.log_softmax(outputs),labels)
        val_loss+=loss.data[0]
    
    val_loss_vs_epoch.append(val_loss/len(val_loader))
    
    plt.plot(train_loss_vs_epoch,'r',val_loss_vs_epoch,'b')
    plt.savefig('plot.png')
        
        

    plt.plot(train_loss_vs_epoch,'r')
    plt.savefig('plt.png')

        
