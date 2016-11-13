#coding utf-8

a = 'ad fkd fdlfjsjiatianbo is dfl jh dkfandsome sdfj l'
search = 'jiatianboishandsome'

u = set(a)
print u
u.update(search)
print len(set(a))==len(u)
