from model.group import Group
from timeit import timeit


def test_group_list(app, db):
    print(timeit(lambda: app.group.get_group_list(), number=1))
    # print("\nui_list: ")
    # print(app.group.get_group_list())
    # print("db_list: ")
    # print(db.get_group_list())

    def clean(group):
        return Group(element_id=group.element_id, name=group.name.strip())

    print("test-009")

    print(timeit(lambda: map(clean, db.get_group_list()), number=1))
    #assert False  # sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)
