import sqlite3

class settings:
    '''
    store db settings
    '''
    db_file = 'student.db'

class db:
    def connect(self):
        return sqlite3.connect(settings.db_file)

    def insert_student(self, student):
        with self.connect() as connect:
            try:
                cursor = connect.cursor()
                cursor.execute(
                "INSERT into student (name, lastname, secondname, sex) \
                values (?,?,?,?);",
                (student.name, student.lastname, student.secondname, student.sex,))
                cursor.execute("Select last_insert_rowid();")
                row = cursor.fetchall()
                student.id = int(row[0][0]) # get inserted student id
                connect.commit()
            except Exception as ex:
                print(ex)

    def delete_student(self, student):
        with self.connect() as conn:
            try:
                cursor = conn.cursor()
                cursor.execute('DELETE from student where id = ?',(student.id,))
                cursor.commit()
            except Exception as ex:
                print(ex)

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
                