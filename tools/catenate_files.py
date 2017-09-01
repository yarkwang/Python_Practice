'''
Created on 2017年8月17日

@author: yark
'''
# coding=utf8
import os

path='20170824'
output='import20170824.txt'

with open(output, 'wb') as outfile:
    for file in os.listdir(path):
        with open(os.path.join(path,file), 'rb') as infile:
            outfile.write(infile.read())