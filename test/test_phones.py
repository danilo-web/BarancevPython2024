from model.contact import Contact


def test_phone_on_home_page(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test", lastname="test"))
    contact_from_homepage = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_homepage.homephone == contact_from_edit_page.homephone
    assert contact_from_homepage.mobilephone == contact_from_edit_page.mobilephone
    assert contact_from_homepage.workphone == contact_from_edit_page.workphone
    assert contact_from_homepage.fax_phone == contact_from_edit_page.fax_phone
