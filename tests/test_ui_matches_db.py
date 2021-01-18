from model.group import Group


def test_group_list(app, db):
    ui_list = app.group.get_groups_list()

    def clean(group):
        return Group(group_id=group.group_id, name=" ".join(group.name.strip().split()))

    db_list = list(map(clean, db.get_groups_list()))
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)
