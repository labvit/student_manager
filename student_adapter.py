class student_adapter(list):
    '''
    This class represents student class as a row in Sheet table.
    A Sheet tkinter class stores only list data correctly
    '''
    def __init__(s, st, db):
        s.db = db
        s.student = st
        # inner scheme to map student fields to array
        s.list = ["name", "lastname", "secondname", "sex"]
        
    def __len__(s):
        '''
        list emulation
        '''
        return len(s.list)

    def __getitem__(s,index):
        return s.student.__getattribute__(s.list[index]) #.get()

    def __setitem__(s,index,value):
        # make a copy to ensure that db correctly updates the student
        student = s.student.copy()
        # think: find more effective method to get/set values 
        student.__setattr__(s.list[index],value)

        if(student.id == 0):
            s.db.insert_student(student)
        else:
            s.db.update_student(student)

        s.student = student

