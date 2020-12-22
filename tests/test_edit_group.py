from model.group import Group


def test_edit_group_name(app):
    if not app.group.count():
        app.group.create(Group(name="tmp"))
    app.group.edit_first_group(Group(name='new name'))


def test_edit_group_header(app):
    if not app.group.count():
        app.group.create(Group(name="tmp"))
    app.group.edit_first_group(Group(header='new header'))