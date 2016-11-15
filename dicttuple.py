#coding utf-8

def test(a,b,c,d,*z,**kr):
	return z,kr

print test(1,2,3,4,5,[1,2,3],g=1,e=2)


#zhuyi abc  ge
