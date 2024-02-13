import re
from random import randrange
from model.contact import Contact


def test_contact_data_on_home_page(app):
    app.contact.open_contact_page()  # По какой-то причине не запуске всех тестов
                                     # не происходит возврат на хом пейдж и тест падает
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="NAME", lastname="LASTNAME", address="address", homephone="1111111",
                                   mobilephone="222", workphone="333", email="E1", email2="E2", email3="E3"))
    index = randrange(len(app.contact.get_contact_list()))
    contact_from_homepage = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_homepage.firstname == contact_from_edit_page.firstname
    assert contact_from_homepage.lastname == contact_from_edit_page.lastname
    assert contact_from_homepage.address == contact_from_edit_page.address
    assert contact_from_homepage.all_phones_from_homepage == merge_phones_like_on_homepage(contact_from_edit_page)
    assert contact_from_homepage.all_emails_from_homepage == merge_emails_like_on_homepage(contact_from_edit_page)

    print('\n' "id = " + str(index))
    print("from_homepage:  " + '\n' + str(contact_from_homepage.all_phones_from_homepage) + '\n' +
                                      str(contact_from_homepage.all_emails_from_homepage))
    print("from_edit_page: " + '\n' + str(merge_phones_like_on_homepage(contact_from_edit_page) + '\n' +
                                      str(merge_emails_like_on_homepage(contact_from_edit_page))))


def clear(s):
    if s is None:
        return None
    return re.sub("[() -]", "", s)


def merge_phones_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone]))))


def clear_emails(s):
    if s is None:
        return None
    return re.sub("[() !?]", "", s)


def merge_emails_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear_emails(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))


# def test_phone_on_contact_view_page(app):
#     # if app.contact.count() == 0:
#     #     app.contact.create(Contact(firstname="test", lastname="test"))
#     contact_from_view_page = app.contact.get_contact_from_view_page(0)  # [0]
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#     assert contact_from_view_page.homephone == contact_from_edit_page.homephone
#     assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
#     assert contact_from_view_page.workphone == contact_from_edit_page.workphone
#     assert contact_from_view_page.fax_phone == contact_from_edit_page.fax_phone