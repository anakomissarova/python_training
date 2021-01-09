from model.group import Group
from random import randrange


def test_edit_group_constant_data(app, json_constant_groups_to_edit):
    if not app.group.count():
        app.group.create(Group(name="tmp"))
    old_groups = app.group.get_groups_list()
    index = randrange(len(old_groups))
    new_group = json_constant_groups_to_edit
    new_group.group_id = old_groups[index].group_id
    app.group.edit_group_by_index(index, new_group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_groups_list()
    old_groups[index] = new_group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_edit_group_random_data(app, data_random_groups):
    if not app.group.count():
        app.group.create(Group(name="tmp"))
    old_groups = app.group.get_groups_list()
    index = randrange(len(old_groups))
    new_group = data_random_groups
    new_group.group_id = old_groups[index].group_id
    app.group.edit_group_by_index(index, new_group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_groups_list()
    old_groups[index] = new_group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
