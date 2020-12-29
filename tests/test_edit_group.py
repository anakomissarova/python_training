from model.group import Group
from random import randrange


def test_edit_group_name(app):
    if not app.group.count():
        app.group.create(Group(name="tmp"))
    old_groups = app.group.get_groups_list()
    index = randrange(len(old_groups))
    new_group = Group(name='new name')
    new_group.group_id = old_groups[index].group_id
    app.group.edit_group_by_index(index, new_group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_groups_list()
    old_groups[index] = new_group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_edit_group_header(app):
    if not app.group.count():
        app.group.create(Group(name="tmp"))
    old_groups = app.group.get_groups_list()
    app.group.edit_first_group(Group(header='new header'))
    new_groups = app.group.get_groups_list()
    assert len(old_groups) == len(new_groups)
