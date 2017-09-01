'''
Created on 20170816

@author: yark
'''
# coding=utf8
from os import listdir, remove
from os.path import isfile, join, splitext, getsize, isdir
import subprocess, hashlib

def getLength(filename):
    result=subprocess.Popen(["ffprobe", filename],
        stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return [x for x in result.stdout.readlines() if b"Duration" in x]

def md5(filename):
    hash_md5=hashlib.md5()
    with open(filename, 'rb') as f:
        for chunk in iter(lambda: f.read(8192), b''):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

path="F:\download\英国BBCphonics发音动画片Alphablocks\Alphablocks第四季"
keyword='幼教，英语，自然拼读法，英音'
description='Alphablocks is a British CGI-animated children''s educational television programme that tries to teach children how to spell with the use of animated blocks representing each letter. It is animated by Blue-Zoo and produced by Alphablocks Ltd. Once the Alphablocks discover that whenever they make a word it comes to life, many new adventures in Alphaland can be created. This is meant to help preschool children with learning the alphabet, spelling, reading and writing.'
export_file='import2017082404.txt'

try:
    remove(export_file)
except OSError:
    pass
f=open(export_file, 'a', encoding='utf-8')

for file in listdir(path):
    if isdir(join(path, file)):
        print(file + ' is a directory')
        continue
    if file[file.rfind('.')+1:]=='srt':
        print(file + '是字幕文件')
        continue
    if isfile(join(path, file)):
        '''file_name'''
        print(file[:file.rfind('.')])
        f.write(file[:file.rfind('.')])
        f.write('|')
        '''file_extension'''
        print(file[file.rfind('.')+1:])
        f.write(file[file.rfind('.')+1:])
        f.write('|')
        '''md5'''
        md5sum=md5(join(path, file))
        print(md5sum)
        f.write(md5sum)
        f.write('|')
        '''position'''
        print(path[path.rfind('\\')+1:])
        f.write(path[path.rfind('\\')+1:])
        f.write('|')        
        '''length'''
        print(b''.join(getLength(join(path, file))).decode('utf8')[12:20]) 
        f.write(b''.join(getLength(join(path, file))).decode('utf8')[12:20]) 
        f.write('|')
        '''size'''
        print('{0:,}'.format(getsize(join(path, file))))
        f.write('{0:,}'.format(getsize(join(path, file))))
        f.write('|')
        '''keyword'''
        print(keyword)
        f.write(keyword)
        f.write('|')
        '''description'''
        print(description)
        f.write(description)
        f.write('\n')

