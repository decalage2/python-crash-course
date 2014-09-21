class Person:

    def __init__(self, lastname, firstname, age, children=None):
        self.lname = lastname
        self.fname = firstname
        self.age = age
        self.children = children
        if children == None:
            self.children = []

    def get_fullname(self):
        return '%s %s' % (self.fname, self.lname)

    def add_years(self, years):
        self.age += years

john = Person('Doe', 'John', 45)
print john.get_fullname()
john.add_years(2)
