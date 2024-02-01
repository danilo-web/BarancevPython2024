from model.contact import Contact


def test_create_new_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="test", middlename="mmmiddlename", lastname="test",
                               nickname="test", title="twst", company="test", address="test", home="77777777",
                               mobile="888888888", work="9999999", fax="555555", email="test", email2="test",
                               email3="test"))
    app.session.logout()
