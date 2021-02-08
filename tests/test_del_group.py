from model.group import Group
import random
import allure


def test_delete_group(app, db, check_ui):
    with allure.step('Given a non-empty group list'):
        if app.group.count() == 0:
            app.group.create(Group(name="tmp"))
        old_groups = db.get_groups_list()
    with allure.step('Given a random group from the list'):
        group = random.choice(old_groups)
    with allure.step('When I delete group %s from the list' % group):
        app.group.delete_group_by_id(group.group_id)
    with allure.step('Then the new group list is equal to the old list without the deleted group'):
        new_groups = db.get_groups_list()
        old_groups.remove(group)
        assert old_groups == new_groups
        if check_ui:
            assert sorted(map(app.group.clear_from_spaces, new_groups), key=Group.id_or_max) == \
                   sorted(app.group.get_groups_list(), key=Group.id_or_max)
