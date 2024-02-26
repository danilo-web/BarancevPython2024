import random
from random import randrange
from model.group import Group


def test_delete_random_group(app, db):
    for i in range(10):
        if len(db.get_group_list()) == 0:
            app.group.create(Group(name="NEW_test"))
        old_groups = db.get_group_list()
        group = random.choice(old_groups)
        # index = randrange(len(old_groups))
        app.group.delete_group_by_id(group.element_id)
        new_groups = db.get_group_list()
        assert len(old_groups) - 1 == app.group.count()
        old_groups.remove(group)
        assert old_groups == new_groups
        # assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
