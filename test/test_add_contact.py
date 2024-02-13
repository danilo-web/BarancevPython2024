from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10 + "-"  # + string.punctuation
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_name(prefix, maxlen):
    symbols = string.ascii_lowercase + string.ascii_uppercase + "-"
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_phone_number(maxlen):
    symbols = string.digits + "-" + " " + "+" + "(" + ")"
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", middlename="", lastname="", nickname="",
                      title="", company="", address="", homephone="", mobilephone="",
                      workphone="", fax_phone="", email="", email2="", email3="")] + [
    Contact(firstname=random_name("firstname", 10), middlename=random_name("middlename", 10),
            lastname=random_name("lastname", 10), nickname=random_name("nickname", 10),
            title=random_name("title", 10), company=random_string("company", 10),
            address=random_string("address", 10), homephone=random_phone_number(10),
            mobilephone=random_phone_number(10), workphone=random_phone_number(10),
            fax_phone=random_phone_number(10), email=random_string("email", 10),
            email2=random_string("email2", 10), email3=random_string("email3", 10))
    for i in range(10)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_create_new_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

    print(new_contacts)
