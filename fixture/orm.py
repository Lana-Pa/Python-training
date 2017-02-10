from pony.orm import *
from datetime import datetime
from model.group import Group
from model.contact import Contact

from pymysql.converters import encoders, decoders, convert_mysql_timestamp



class ORMFixture:
    db = Database()

    class ORMGroup(db.Entity):
        _table_ = 'group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')
        contacts = Set(lambda: ORMFixture.ORMContact, table='address_in_groups', column='id', reverse="groups", lazy=True) # устанавливаем связь между группами и контактами, set - множество (quantity)



    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        lastname = Optional(str, column='lastname')
        address = Optional(str, column='address')
        email = Optional(str, column='email')
        email2 = Optional(str, column='email2')
        email3 = Optional(str, column='email3')
        home = Optional(str, column='home')
        mobile = Optional(str, column='mobile')
        work = Optional(str, column='work')
        phone2 = Optional(str, column='phone2')
        deprecated = Optional(datetime, column='deprecated')
        groups = Set(lambda: ORMFixture.ORMGroup, table='address_in_groups', column='group_id', reverse="contacts", lazy=True)

    # connect db
    def __init__(self, host, name, user, password):
        conv = encoders
        conv.update(decoders)
        conv[datetime] = convert_mysql_timestamp
        self.db.bind('mysql', host=host, database=name, user=user, password=password, autocommit=True, conv=conv)
        self.db.generate_mapping()
        sql_debug(True) # to see the real sql-statement

    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)

        return list(map(convert, groups))

    def convert_contacts_to_model(self, contacts):
        def convert(contact):
            return Contact(id=str(contact.id), firstname=contact.firstname, lastname=contact.lastname, address=contact.address,
                           home_phone=contact.home, mobile_phone=contact.mobile, work_phone=contact.work, phone2=contact.phone2,
                           email1=contact.email, email2=contact.email2, email3=contact.email3)

        return list(map(convert, contacts))

    @db_session
    def get_group_list(self):
        # with db_session:
            return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup)) # equals Select ...from ... where...

    @db_session
    def get_contact_list(self):
        # with db_session:
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None)) # equals Select ...from

    @db_session
    def get_contacts_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        # return self.convert_contacts_to_model(orm_group.contacts)

        # попытка выбрать только неудаленные файлы по аналогии с not_in_group - не работает
        return self.convert_contacts_to_model(
             select(c for c in ORMFixture.ORMContact if c.deprecated is None and orm_group in c.groups))

    @db_session
    def get_contacts_not_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]
        return self.convert_contacts_to_model(
            select(c for c in ORMFixture.ORMContact if c.deprecated is None and orm_group not in c.groups))








