#coding utf-8

a = {'a':'haha','b':'xixi','d':'haha','c':'xiaxia','e':'haha'}

search_value = 'haha'

key_list = []

for x,y in a.items():
	print x,y
	if y == search_value:
		key_list.append(x)
print key_list
