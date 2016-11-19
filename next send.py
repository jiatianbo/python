def test():
    x = yield 1
    print 2,x
    x = yield 3
    print 4,x

t = test()
print t.next()
print t.send('6')
