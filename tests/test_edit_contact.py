from model.contact import Contact


def test_edit_contact(app):
    app.contact.edit_first_contact(Contact(firstname=" 1", lastname="Lastname"))
