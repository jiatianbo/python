def febir(num):
    x,y = 1,1
    while x < num:
        yield x
        x,y = y,x+y

for i in febir(13):
    print i