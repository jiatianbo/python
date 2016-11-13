#coding utf-8

a = 'a lfj df k	7667dfalDKFJ 656LLFAA LAD FK'
l =sorted(a)

a_upper_list = []
a_lower_list = []

for x in l:
	if x.isupper():
		a_upper_list.append(x)
	elif x.islower():
		a_lower_list.append(x)
	else:
		pass
for y in a_upper_list:
	y_lower = y.lower()
	if y_lower in a_lower_list:
		a_lower_list.insert(a_lower_list.index(y_lower),y)
print ''.join(a_lower_list)
