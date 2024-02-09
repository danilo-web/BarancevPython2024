from model.contact import Contact


def test_create_new_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="firstname", middlename="mmmiddlename", lastname="lastname", nickname="test",
                      title="twst", company="test", address="test", homephone="77777777", mobilephone="888888888",
                      workphone="9999999", fax_phone="555555", email="test", email2="test", email3="test")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

    print(new_contacts)
