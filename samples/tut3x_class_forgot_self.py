# Python tutorial - method with missing "self" argument

class Person:

    def __init__(self, lastname, firstname):
        self.lname = lastname
        self.fname = firstname

    def display():
        print "Last name: %s - First name: %s" % \
              (self.lname, self.fname)



jd = Person('Doe', 'John')
jd.display()


# Typical error message when this script is run:
##>>>
##Traceback (most recent call last):
##  File "C:\Users\user\Documents\Python tutorial\tut3x_class_forgot_self.py", line 15, in <module>
##    jd.display()
##TypeError: display() takes no arguments (1 given)
##>>>
