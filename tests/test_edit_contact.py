from model.contact import Contact


def test_edit_contact(app):
    if not app.contact.count():
        app.contact.create(Contact(firstname="tmp"))
    app.contact.edit_first_contact(Contact(firstname=" 1", lastname="Lastname"))
