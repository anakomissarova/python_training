from model.group import Group
import random


def test_edit_group_constant_data(app, db, json_constant_groups_to_edit, check_ui):
    if not app.group.count():
        app.group.create(Group(name="tmp"))
    old_groups = db.get_groups_list()
    new_group = json_constant_groups_to_edit
    new_group.group_id = random.choice(old_groups).group_id
    app.group.edit_group_by_id(new_group)
    new_groups = db.get_groups_list()
    for group in old_groups:
        if group.group_id == new_group.group_id:
            old_groups.remove(group)
            break
    old_groups.append(new_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(map(app.group.clear_from_spaces, new_groups), key=Group.id_or_max) == \
               sorted(app.group.get_groups_list(), key=Group.id_or_max)


def test_edit_group_random_data(app, db, data_random_groups, check_ui):
    if not app.group.count():
        app.group.create(Group(name="tmp"))
    old_groups = db.get_groups_list()
    new_group = data_random_groups
    new_group.group_id = random.choice(old_groups).group_id
    app.group.edit_group_by_id(new_group)
    new_groups = db.get_groups_list()
    for group in old_groups:
        if group.group_id == new_group.group_id:
            old_groups.remove(group)
            break
    old_groups.append(new_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(map(app.group.clear_from_spaces, new_groups), key=Group.id_or_max) == \
               sorted(app.group.get_groups_list(), key=Group.id_or_max)
