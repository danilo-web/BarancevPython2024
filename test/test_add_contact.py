from model.contact import Contact


def test_create_new_contact(app):
    app.contact.create(Contact(firstname="test", middlename="mmmiddlename", lastname="test",
                               nickname="test", title="twst", company="test", address="test", home="77777777",
                               mobile="888888888", work="9999999", fax="555555", email="test", email2="test",
                               email3="test"))


def test_create_new_another_contact(app):
    app.contact.create(Contact(firstname="ABC", middlename="ABC", lastname="ABC",
                               nickname="ABC", title="ABC", company="ABC", address="test", home="ABC",
                               mobile="ABC", work="ABC", fax="ABC", email="ABC", email2="ABC",
                               email3="ABC"))
