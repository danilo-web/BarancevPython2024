from model.group import Group


def test_delete_first_group(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name="NEW_test"))
    app.group.delete_first_group()
    new_groups = app.group.get_group_list()
    len_old_group = len(old_groups)
    if len_old_group == 0:  # на случай если нет групп то тест на колличество падает потому что 0-1=-1
        len_old_group = len_old_group + 1
    assert len_old_group - 1 == len(new_groups)
    old_groups[0:1] = []
    assert old_groups == new_groups
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    print(str(old_groups))
