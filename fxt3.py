#coding=utf-8

def getitem(*kargs):
    return kargs

l = getitem(1,2,3,4,5)
for x in l:
    print(x,end=' ')

print('')

l = getitem(5,6,4,7,2)
for x in l:
    print(x,end=' ')