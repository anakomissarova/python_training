from model.group import Group


def test_add_group(app, db, json_groups, check_ui):
    group = json_groups
    old_groups = db.get_groups_list()
    app.group.create(group)
    new_groups = db .get_groups_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(map(app.group.clear_from_spaces, new_groups), key=Group.id_or_max) == \
               sorted(app.group.get_groups_list(), key=Group.id_or_max)
