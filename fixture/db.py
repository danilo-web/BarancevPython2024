import pymysql.connections
from model.group import Group
from model.contact import Contact


class Dbfixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        db_group_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (element_id, name, header, footer) = row
                db_group_list.append(Group(element_id=str(element_id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return db_group_list

    def get_contact_list(self):
        db_group_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname from addressbook where deprecated is null ")
            for row in cursor:
                (element_id, firstname, lastname) = row
                db_group_list.append(Contact(element_id=str(element_id), firstname=firstname, lastname=lastname))
        finally:
            cursor.close()
        return db_group_list

    def destroy(self):
        self.connection.close()
