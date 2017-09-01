'''
Created on 2017年7月4日

@author: wei.wang7
'''
import os

cwd="D:\\download"
# for filename in os.listdir(cwd):
#     if filename.startswith("[电影天堂www.dy2018.com]"): #20 chars
#         os.rename(cwd+"\\"+filename, cwd+"\\"+filename[20:])

for filename in os.listdir(cwd):
    if filename.startswith("[大军SS马懿之军S联M]"):
        os.rename(cwd+"\\"+filename, cwd+"\\"+"[大军师司马懿之军师联盟]"+filename[13:])