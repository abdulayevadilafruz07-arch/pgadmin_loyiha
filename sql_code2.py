import psycopg2
from psycopg2 import connect

import psycopg2


class Data_connect:
    def __init__(self):
        self.connection = psycopg2.connect(
            dbname='n71_baza',
            user='n71_admin',
            password='123',
            host='localhost',
            port=5432
        )

        self.cursor = self.connection.cursor()


    def add_contact(self, name, contact):
        query = """
        INSERT INTO contacts (name, contact)
        VALUES (%s, %s)
        """
        self.cursor.execute(query, (name, contact))
        self.connection.commit()
    def create_table(self):
        s='''
        create table test(
        id serial primary key,
        name varchar(50));
        '''
        self.cursor.execute(s,)
        self.connection.commit()
    def contact_view(self):
        s ='''
        select * from contacts;
        '''
        self.cursor.execute(s)
        con = self.cursor.fetchall()
        for item in con:
            print(item[0],item[1],item[2])

    def del_contact(self,id):
        s='''
        delete from contacts where id=(%s)
        '''
        self.cursor.execute(s,(id,))
        self.connection.commit()

My_object = Data_connect()
#
# My_object.add_contact("ali","12345678")
# My_object.contact_view()
# My_object.del_contact(1)
# while True:
#     menu = input("menu: ")
#     if menu == "1":
#         model = input("model name: ")
#         title = input("title: ")
#         My_object.add_car(model, title)
#
# connecter = DB_connecter()
# connecter.Create_car("Model", "Title")
#
def contact_manager():
    while True:
        code = input("code: ")

        if code == "1":
            name = input("name: ")
            contact = input("contact: ")
            My_object.add_contact(name,contact)
        elif code=="2":
            My_object.contact_view()
        elif code=="3":
            My_object.contact_view()
            id  =int(input("id: "))
            My_object.del_contact(id)
            print(id ,"o'chirildi")
        else:
            break
contact_manager()

#
#
# # Menager_auto_salon()
#
#
