#coding utf-8

a = 'aALDFASLKdkfsdksd l'
a_list = list(a)
set_list = list(set(a_list))
set_list.sort(key=a_list.index)
print set_list
print ''.join([x for x in set_list])
