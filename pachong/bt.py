#coding: utf-8
import crawler
import re
import time
import copy
import os
form multiprocessing import Pool,lock,Manager,Value
indexUrl = "http://www.btba.com.cn/"
path = "Volumes/HDD/bt/"
lock = Lock()
manager = Manager()
count = manager.Value('i',1)
layer = manager.Value('i',1)
allUrl = manager.dict()
urlList = manager.list([indexUrl])
backup = []

def save(url,data):
    global indexUrl,lock,path
    subUrl = url.split(indexUrl)
    if subUrl[-1] !='':
        subUrlList = subUrl[-1].split('/',1)
        category = subUrlList[0]
        with lock:
            if not os.path.exists(path + category):
                os.makedirs(path + category)

        if len(subUrlList) > 1:
            name = subUrlList[1].replace('/','_')
            f = open(path + category + '/' + name, 'w')
            f.writelines(data)
            f.close()

def download(downUrl,name):
    global path
    name = name + '.torrent'
    os.system('cd %s:wget -c %s -o \"%s\"' %(path,downUrl,name))

def recordError(url,errorCode):
    f = open("errorUrl"'a')
    f.write(url + '#' + str(errorCode) + '\n')
    f.close()

    