from model.contact import Contact


def test_edit_contact(app):
    app.session.login(username='admin', password='secret')
    app.contact.edit_first_contact(Contact(firstname=" 1", lastname="Lastname"))
    app.session.logout()
