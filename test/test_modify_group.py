from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="New_group_for_TEST", header="test"))
    old_groups = app.group.get_group_list()
    group = Group(name="UPDATED_EDITED")
    group.element_id = old_groups[0].element_id
    app.group.modify_first_group(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

    print(new_groups)


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(header="test"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(header="UPDATED_EDITED"))
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

    print(new_groups)
