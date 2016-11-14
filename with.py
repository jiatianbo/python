#coding utf-8

g = open('a.txt','w')
g.write('jiatianbo')
g.close()

with open('a.txt','a') as g:
	g.write(' is handsome')
