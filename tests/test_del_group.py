from model.group import Group
import random


def test_delete_group(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name="tmp"))
    old_groups = db.get_groups_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.group_id)
    assert len(old_groups) - 1 == app.group.count()
    new_groups = db.get_groups_list()
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(map(app.group.clear_from_spaces, new_groups), key=Group.id_or_max) == \
               sorted(app.group.get_groups_list(), key=Group.id_or_max)
