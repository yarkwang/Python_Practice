'''
Created on 2017年9月6日

@author: wei.wang7
'''
from os import listdir
from os.path import join, isdir
import os

path="D:\美语世界AVI视频及mp3（备份）\PLAY ALONG"

for file in listdir(path):
    if isdir(join(path, file)):
        continue;
    if file[file.rfind('.')+1:]!='avi':
        continue
    print('python get_viedo_thumbnail.py ' + '"' + (join(path, file)) + '"  "' + (join(path, file[:file.rfind('.')])+'.jpg') + '"')
    os.system('python get_viedo_thumbnail.py ' + '"' + (join(path, file)) + '"  "' + (join(path, file[:file.rfind('.')])+'.jpg') + '"')
        
    