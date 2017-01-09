# coding: utf-8
import crawler
import re
import time
import copy
import os
from multiprocessing import Pool, Lock, Manager, Value

indexUrl = "http://www.btba.com.cn/"
path = "/Volumes/HDD/bt/"
lock = Lock()
manager = Manager()
count = manager.Value('i', 1)
layer = manager.Value('i', 1)
allUrl = manager.dict()
urlList = manager.list([indexUrl])
backup = []

# def save(url, data):
# 	global indexUrl, lock, path
# 	subUrl = url.split(indexUrl)
# 	if subUrl[-1] != '':
# 		subUrlList = subUrl[-1].split('/', 1)
# 		category = subUrlList[0]
# 		with lock:
# 			if not os.path.exists(path + category):
# 				os.makedirs(path + category)
# 		if len(subUrlList) > 1:
# 			name = subUrlList[1].replace('/', '_')
# 			f = open(path + category + '/' + name, 'w')
# 			f.writelines(data)
# 			f.close()

def download(downUrl, name):
	global path
	name = name + '.torrent'
	os.system('cd %s;wget -c %s -O \"%s\"' % (path, downUrl, name))

def recordError(url, errorCode):
	f = open("errorUrl", 'a')
	f.write(url + '#' + str(errorCode) + '\n')
	f.close()

def parseUrl(data):
	global indexUrl
	pattern = re.compile(r'\"%s[\s\S]*?\"' % indexUrl)
	l = pattern.findall(data)
	return l

def getDownInfo(data):
	global count
	pattern = re.compile(r'function down[\s\S]*?torrent[\s\S]*?\"')
	fnDown = pattern.search(data)
	downUrl = False
	title = "NotFound" + str(count)
	if fnDown:
		pattern = re.compile(r'\"http://torrent\.[\s\S]*?\"')
		url = pattern.search(fnDown.group())
		if url:
			downUrl = url.group()
			pattern = re.compile(r'<title>[\s\S]*?</title>')
			t = pattern.search(data)
			if t:
				title = t.group().split('>')[1].split('<')[0]
	return downUrl, title

def run(url):
	global allUrl, urlList, count, layer
	data = crawler.urlopen(url)
	if type(data) == str and not url in allUrl:
		allUrl[url] = True
		#save(url, data)
		tmpList = parseUrl(data)
		for x in tmpList:
			x = x[1:-1]
			if not x in allUrl:
				urlList.append(x)
		downUrl, title = getDownInfo(data)
		if downUrl:
			download(downUrl, title)

	elif type(data) == int:
		recordError(url, data)
		

if __name__ == '__main__':
	p = Pool(10)
	while len(urlList) > 0:
		backup = copy.deepcopy(urlList)
		del urlList[:]
		p.map(run, backup)
	p.close()
	p.join()