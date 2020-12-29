from model.group import Group


def test_edit_group_name(app):
    if not app.group.count():
        app.group.create(Group(name="tmp"))
    old_groups = app.group.get_groups_list()
    new_group = Group(name='new name')
    new_group.group_id = old_groups[0].group_id
    app.group.edit_first_group(new_group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_groups_list()
    old_groups[0] = new_group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_edit_group_header(app):
    if not app.group.count():
        app.group.create(Group(name="tmp"))
    old_groups = app.group.get_groups_list()
    app.group.edit_first_group(Group(header='new header'))
    new_groups = app.group.get_groups_list()
    assert len(old_groups) == len(new_groups)
