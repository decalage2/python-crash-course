
class Person:

    def __init__(self, lastname, firstname):
        self.lname = lastname
        self.fname = firstname

    def get_fullname(self):
        return '%s %s' % (self.fname, self.lname)

    def display(self):
        print self.get_fullname()

    def __str__(self):
        return "Last name: %s - First name: %s" % \
              (self.lname, self.fname)


p = Person('Doe', 'John')
p.display()
print p

