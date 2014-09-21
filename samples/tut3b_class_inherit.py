
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



jd = AddrBookPerson('Doe', 'John', 'Chicago')
jd.display()
jd.display_address()

jd.move('San Francisco')
jd.display_address()

jd.set_postcode('12345')
jd.display_postcode()