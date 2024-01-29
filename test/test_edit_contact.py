from model.contact import Contact


def test_edit_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit(Contact(firstname="EDITED", middlename="EDITED", lastname="EDITED",
                             nickname="EDITED", title="TITLE", company="test", address="test", home="03",
                             mobile="7-7-7-7-7-7-7-7", work="01", fax="02", email="email", email2="test",
                             email3="test", homepage="test", bday="21", bmonth="June", byear="2001"))
    app.session.logout()
