#coding=utf-8

def add(*num):
    print num
    s = 0
    for x in num:
        s+=x
    return s

print add(1,2,3,4,5)
print add(1,2,3)