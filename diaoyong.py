#encoding=utf-8

def fun(a):
	print 'id %d' % id(a)
a = [1,2,3]
print 'start'
print id(a)

fun(a)
