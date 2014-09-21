
class Person:

    def __init__(self, lastname, firstname):
        self.lname = lastname
        self.fname = firstname

    def display(self):
        print "Last name: %s - First name: %s" % \
              (self.lname, self.fname)

    def __str__(self):
        return "Last name: %s - First name: %s" % \
              (self.lname, self.fname)


class AddrBookPerson (Person):

    def __init__(self, lastname, firstname, address):
        Person.__init__(self, lastname, firstname)
        self.addr = address

    def display_address(self):
        print self.addr

    def move(self, new_address):
        self.addr = new_address

    def set_postcode(self, postcode):
        self.postcode = postcode

    def display_postcode(self):
        print self.postcode

##pl = Person('lagadec', 'philippe')
###pl.display()
##print pl
##
##jc = AddrBookPerson('Gallard', 'JC', 'The Hague')
##jc.display()
##jc.display_address()
##
##jc.move('Wassenaar')
##jc.display_address()
##
##jc.set_postcode('1234AB')
##jc.display_postcode()