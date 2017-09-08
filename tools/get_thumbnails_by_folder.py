'''
Created on 2017年9月6日

@author: wei.wang7
'''
# coding=utf8

from os import listdir
from os.path import join, isdir
import os

path="F:\download\小猪佩奇\粉红猪小妹中文版-[720P]共4季\粉红猪小妹第2季52集[720p]"

for file in listdir(path):
    if isdir(join(path, file)):
        continue;
    if file[file.rfind('.')+1:]!='mp4':
        continue
    print('python get_viedo_thumbnail.py ' + '"' + (join(path, file)) + '"  "' + (join(path, file[:file.rfind('.')])+'.jpg') + '"')
    os.system('python get_viedo_thumbnail.py ' + '"' + (join(path, file)) + '"  "' + (join(path, file[:file.rfind('.')])+'.jpg') + '"')
        
    