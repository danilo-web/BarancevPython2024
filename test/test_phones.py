import re
from model.contact import Contact


def test_contact_data_on_home_page(app):
    app.contact.open_contact_page()  # По какой-то причине не запуске всех тестов
                                     # не происходит возврат на хом пейдж и тест падает
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test", lastname="test"))
    contact_from_homepage = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    print('\n' + "1 - contact_from_homepage.all_phones_from_homepage - " + str(contact_from_homepage.all_phones_from_homepage))
    print("2 - contact_from_edit_page - " + str(merge_phones_like_on_homepage(contact_from_edit_page)))
    print("3 - contact_from_homepage.all_emails_from_homepage - " + str(contact_from_homepage.all_emails_from_homepage))
    print("4- merge_emails_like_on_homepage(contact_from_edit_page) - " + str(merge_emails_like_on_homepage(contact_from_edit_page)))

    assert contact_from_homepage.all_phones_from_homepage == merge_phones_like_on_homepage(contact_from_edit_page)
    assert contact_from_homepage.all_emails_from_homepage == merge_emails_like_on_homepage(contact_from_edit_page)


# def test_phone_on_home_page(app):
#     # if app.contact.count() == 0:
#     #     app.contact.create(Contact(firstname="test", lastname="test"))
#     contact_from_homepage = app.contact.get_contact_list()[0]
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#     print("contact_from_homepage.all_phones_from_homepage - " + str(contact_from_homepage.all_phones_from_homepage))
#     print("contact_from_edit_page - " + str(contact_from_edit_page))
#     assert contact_from_homepage.all_phones_from_homepage == merge_phones_like_on_homepage(contact_from_edit_page)


# def test_phone_on_contact_view_page(app):
#     # if app.contact.count() == 0:
#     #     app.contact.create(Contact(firstname="test", lastname="test"))
#     contact_from_view_page = app.contact.get_contact_from_view_page(0)  # [0]
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
#     assert contact_from_view_page.homephone == contact_from_edit_page.homephone
#     assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
#     assert contact_from_view_page.workphone == contact_from_edit_page.workphone
#     assert contact_from_view_page.fax_phone == contact_from_edit_page.fax_phone


def clear(s):
    if s is None:
        return None
    return re.sub("[() -]", "", s)


def merge_phones_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone]))))


def merge_emails_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))
