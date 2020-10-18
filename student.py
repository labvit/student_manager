class student:
    def __init__(self, name = '', lastname = '', secondname='', sex = 0, id = 0):
        '''
        man has 0 sex value
        woman has 1 sex value
        new user has 0 id value
        '''
        self.name = name # value_adapter( name)
        self.lastname =  lastname # value_adapter(lastname)
        self.id = id #  value_adapter(id)
        self.secondname=  secondname # value_adapter(secondname)
        self.sex =  sex #value_adapter(sex)
    def copy(s):
        newstudent = student(s.name, s.lastname, s.secondname, s.sex, s.id)
        return newstudent
    def __str__(s):
        return s.name + " " + s.lastname + " " + (s.secondname if s.secondname is not None else "")

