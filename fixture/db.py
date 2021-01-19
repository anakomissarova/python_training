import pymysql.cursors
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, dbname, user, password):
        self.host = host
        self.dbname = dbname
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=dbname,
                                          user=user, password=password, autocommit=True)

    def destroy(self):
        self.connection.close()

    def get_groups_list(self):
        group_list = []
        with self.connection.cursor() as cursor:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                group_id, name, header, footer = row
                group_list.append(Group(group_id=str(group_id), name=name, header=header, footer=footer))
        return group_list

    def get_contacts_list(self):
        contact_list = []
        with self.connection.cursor() as cursor:
            cursor.execute("""select id, firstname, lastname, address, home, mobile, work, phone2, email, email2, email3 
                              from addressbook where deprecated='0000-00-00 00:00:00'""")
            for row in cursor:
                contact_id, firstname, lastname, address, home, mobile, work, secondary, email1, email2, email3 = row
                contact_list.append(Contact(contact_id=str(contact_id), firstname=firstname, lastname=lastname,
                                            address=address, home=home, mobile=mobile, work=work, secondary=secondary,
                                            email1=email1, email2=email2, email3=email3))
        return contact_list
