# coding -*- utf-8 -*-

from tksheet import Sheet
import tkinter as tk
from student import *
from student_adapter import *
from db_adapter import *

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
        '''
        Add new empty student record
        '''
        s.sheet.insert_row(values=student_adapter(student(),s.db), redraw=True)

mydb = db()
# print([i for i in mydb.get_student()])
app = demo(mydb)
app.mainloop()
