
# open a file for reading:
f = open('tut1a_functions.py')
data = f.read()
f.close()
print data

if 'abc' in data:
    print 'found "abc" in the file.'



# open a file for writing:
fw = open('newfile.txt', 'w')
fw.write('abc\n')
fw.write('def\n')
fw.close()