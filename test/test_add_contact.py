from model.contact import Contact


def test_create_new_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="firstname", middlename="mmmiddlename", lastname="lastname", nickname="test", title="twst",
                      company="test", address="test", home="77777777", mobile="888888888", work="9999999",
                      fax="555555", email="test", email2="test", email3="test")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

    print(new_contacts)
