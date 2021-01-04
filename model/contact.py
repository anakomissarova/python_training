from sys import maxsize


class Contact:
    def __init__(self, contact_id=None, firstname=None, middlename=None, lastname=None, address=None,
                 mobile=None, home=None, work=None, secondary=None, phones_from_homepage=None,
                 email1=None, email2=None, email3=None, emails_from_homepage=None):
        self.contact_id = contact_id
        self.firstname = firstname
        self.middlename = middlename
        self.address = address
        self.lastname = lastname
        self.mobile = mobile
        self.home = home
        self.work = work
        self.secondary = secondary
        self.phones_from_homepage = phones_from_homepage
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        self.emails_from_homepage = emails_from_homepage

    def __eq__(self, other):
        return (self.contact_id == other.contact_id or self.contact_id is None or other.contact_id is None) and \
                self.lastname == other.lastname and \
                self.firstname == other.firstname

    def __repr__(self):
        return "{0}: {1} {2}".format(self.contact_id, self.lastname, self.firstname)

    def compare_ids(self):
        return int(self.contact_id) if self.contact_id else maxsize
