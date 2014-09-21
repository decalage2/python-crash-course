# you may provide default values for arguments:
def mysum(a, b, c=0):
    print "a =",a
    print "b =",b
    print "c =",c
    return a+b+c

s = mysum(1,2,3)
print 'sum:', s
s = mysum(3,4)
print 'sum:', s

