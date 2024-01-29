from model.group import Group


def test_delete_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="EDITED", header="EDITED", footer="EDITED"))
    app.session.logout()
