# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 02:00:53 2018

@author: Trijeet
"""

import os,csv

source="/home/soham/Documents/Deep Learning/hackathon/train_"
dest= "/home/soham/Documents/Deep Learning/hackathon/"

#Adding the sample files to test
## Just a generator for sample testing. To be removed when you have the files.
#csv_path=dest+str("testing.csv")
#f= open(csv_path)
#readob = csv.reader(f)
#for row in readob:
#    if(".png" in row[4]):
#        ff=open(source+row[4],"w+")
#        ff.close()
#f.close()


#Sorting the files to appropriate folders
csv_path="/home/soham/Documents/Deep Learning/hackathon/train.csv"
f= open(csv_path)
readob = csv.reader(f)
for row in readob:
    if(".png" in row[4]): #Just to remove the first line
        classid=int(row[5][6:])
        print classid
        desti=dest+str(classid)
        if os.path.isdir(desti)==False:
            os.makedirs(desti)
        print row[4]
        #os.rename("path/to/current/file.foo", "path/to/new/desination/for/file.foo")
        os.rename(source+"/"+row[4], desti+"/"+row[4])
f.close()
