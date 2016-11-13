#coding utf-8

import os
m = os.popen('python -m this').read()
m = m.replace('\n','')
l =m.split(' ')
print [(x,l.count(x)) for x in ['be','is','than']]
