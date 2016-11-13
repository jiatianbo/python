#coding utf-8

a ='adlf dsf k	dklf slDKFDF FSDJFLAWOIQP'

print dict([(x,a.count(x)) for x in set(a)])
