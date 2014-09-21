def mysum(a,b):
    print "a =",a
    print "b =",b
    return a+b

s = mysum(3,4)
print 'sum:', s
s =  mysum(1,2)
print 'sum:', s

# the function also works with strings:
s = mysum('abc', 'def')
print s

# and even with lists:
lista = [1,2]
listb= ['abc, def']
print mysum(lista, listb)