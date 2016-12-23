
class Global:
    def __init__(self):
        pass;
    def __str__(self):
        s = ''
        for name,value in vars(self).items():
            s += '%s=%s\n'%(name,value)
        return s


g = Global()
g.test = True
g.str = "str"

print g
