from random import randrange
from model.group import Group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="New_group_for_TEST", header="test"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="UPDATED_EDITED")
    group.element_id = old_groups[index].element_id
    app.group.modify_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

    print(new_groups)


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(header="test"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.modify_group_by_index(index, Group(header="UPDATED_EDITED"))
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

    print(new_groups)
