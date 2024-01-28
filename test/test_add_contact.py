from model.contact import Contact
import pytest
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_create_new_contact(app):
    app.session.login(username="admin", password="secret")
    app.create_new_contact(Contact(firstname="test", middlename="mmmiddlename", lastname="test",
                                   nickname="test", title="twst", company="test", address="test", home="77777777",
                                   mobile="888888888", work="9999999", fax="555555", email="test", email2="test",
                                   email3="test", homepage="test", bday="17", bmonth="November", byear="2000"))
    app.session.logout()
