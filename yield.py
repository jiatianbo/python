def test():
    i = 0
    a = 4
    while i < a:
        x = yield i
        i += 1

for i in test():
    print i