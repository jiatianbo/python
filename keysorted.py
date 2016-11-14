#coding utf-8

import string 

a = 'deCvaldfj DFJ dkf d234'
a = ''.join([x for x in a if not x.isdigit()])
print a
print sorted(a,key=string.upper)

a = [string.upper(x) for x in a]
print sorted(a)
