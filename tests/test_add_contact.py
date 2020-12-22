from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname='test', mobile='+78943562435'))





