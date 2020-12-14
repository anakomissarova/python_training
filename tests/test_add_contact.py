from model.contact import Contact


def test_add_contact(app):
    app.session.login(username='admin', password='secret')
    app.contact.create(Contact(firstname='test', mobile='+78943562435'))
    app.session.logout()





