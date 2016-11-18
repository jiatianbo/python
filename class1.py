#coding=utf-8

class Base(object):
    def __init__(self,name):
        self.name = name
class b(Base):
    def get_name(self):
        return self.name
new_class = b('jiatianbo')
print new_class.get_name()