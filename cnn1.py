#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 19:34:00 2018

@author: soham
"""
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

class Net(nn.Module):
    def __init__(self):
        super(Net,self).__init__()
        self.conv1=nn.Conv2d(3,8,5,padding=2)
        self.pool=nn.MaxPool2d(2,2)
        self.conv2=nn.Conv2d(8,16,5,padding=2)
        self.conv3=nn.Conv2d(16,32,5,padding=2)
        self.fc1=nn.Linear(32*28*28,120)
        self.fc2=nn.Linear(120,14)
    
    def forward(self,x):
        x=self.pool(F.relu(self.conv1(x)))
        x=self.pool(F.relu(self.conv2(x)))
        x=self.pool(F.relu(self.conv3(x)))
        x=x.view(-1,32*28*28)
        x=self.fc1(x)
        x=self.fc2(x)
        return x
        
        


        

net=models.resnet18(pretrained=False)
net.fc=nn.Linear(512,14)

criterion=nn.CrossEntropyLoss(size_average=True)
learn_rate=0.1
optimizer=optim.SGD(net.parameters(),lr=learn_rate,momentum=0.9)
net=nn.DataParallel(net)
net=net.cuda()
train_loss_vs_epoch=[]
val_loss_vs_epoch=[]

for epoch in range(15):
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
    
    train_loss_vs_epoch.append(train_loss/14)
    
    for batch in val_loader:
        net=net.train(False)
        inputs,labels=batch
        inputs,labels=Variable(inputs),Variable(labels)
        inputs,labels=inputs.cuda(),labels.cuda()
        outputs=net(inputs)
        loss=criterion(F.log_softmax(outputs),labels)
        val_loss+=loss.data[0]
    
    val_loss_vs_epoch.append(val_loss/14)
    
    plt.plot(train_loss_vs_epoch,'r',val_loss_vs_epoch,'b')
    plt.savefig('plot.png')
        
        

    plt.plot(train_loss_vs_epoch,'r')
    plt.savefig('plt.png')


torch.save(net,'model.pth')
