# coding -*- utf-8 -*-

from tksheet import Sheet
import tkinter as tk
import sqlite3

class settings:
    db_file = 'student.db'

class db:
    def __init__(self):
        pass
    def connect(self):
        return sqlite3.connect(settings.db_file)

    def insert_student(self, student):
        with self.connect() as connect:
            cursor = connect.cursor()
            cursor.execute(
            "INSERT into student (name, lastname, secondname, sex) \
            values (?,?,?,?);",
            (student.name, student.lastname, student.secondname, student.sex,))
            cursor.execute("Select last_insert_rowid();")
            row = cursor.fetchall()
            print(row)
            student.id = int(row[0][0])
            connect.commit()

    def delete_student(self, student):
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE from student where id = ?',(student.id,))
            cursor.commit()

    def get_student(self):
        cur = self.connect().cursor()
        cur.execute(
            "Select  name, lastname, secondname, sex, id from student"
            )
        rows = cur.fetchall()
        for row in rows:
            # print(row)
            yield student(*row)

    def update_student(self, student):
        # print(student)
        with  self.connect() as conn:
            try:
                cur = conn.cursor()
                cur.execute(
                    "UPDATE student set name = ?, \
                    lastname =?, secondname = ?, sex = ? where id = ?",
                    (student.name, student.lastname, student.secondname,student.sex, student.id))
                conn.commit()
            except Exception as ex:
                print(ex)
class value_adapter:
    def __init__(s,value):
        s.value = value
    def set(s,value):
        s.value = value
    def get(s):
        return s.value
    def __str__(s):
        return s.value.__str__()

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

class student_adapter(list):
    def __init__(s, st, db):
        s.db = db
        s.student = st
        s.list = ["name", "lastname", "secondname", "sex"]
        # print(s.list)
    def __len__(s):
        return len(s.list)

    def __getitem__(s,index):
        return s.student.__getattribute__(s.list[index]) #.get()

    def __setitem__(s,index,value):
        student = s.student.copy()
        student.__setattr__(s.list[index],value)

        if(student.id == 0):
            s.db.insert_student(student)
        else:
            s.db.update_student(student)

        s.student = student

class demo(tk.Tk):
    def __init__(s, db):
        tk.Tk.__init__(s)
        s.db = db
        
        s.grid_columnconfigure(0,weight=1)
        s.grid_rowconfigure(0,weight=1)
        s.frame = tk.Frame(s)
        s.addBtn = tk.Button(s.frame, text=u'добавить')
        s.addBtn.grid(row=0,column=0,sticky='nswe')
        s.addBtn.config(command = s.click_event)
        s.frame.grid_rowconfigure(0, weight=1)
        s.frame.grid_columnconfigure(0, weight=1)
        s.sheet = Sheet(s.frame,
            page_up_down_select_row = True,
            column_width = 130,
            data = [student_adapter(student,db) for student in db.get_student()]
            )
        s.sheet.enable_bindings(("single_select",
                                'edit_cell'))

        s.frame.grid(row=0,column=0, sticky = 'nswe')
        s.sheet.grid(row=1,column=0, sticky = 'nswe')
    def click_event(s):
        s.sheet.insert_row(values=student_adapter(student(),s.db), redraw=True)
        # s.sheet.refresh()

mydb = db()
# print([i for i in mydb.get_student()])
app = demo(mydb)
app.mainloop()
