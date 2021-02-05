from pytest_bdd import scenario
from bdd.steps.group_steps import *

FEATURES_PATH = '../features'


@scenario('groups.feature', 'Add new group', features_base_dir=FEATURES_PATH)
def test_add_new_group():
    pass


@scenario('groups.feature', 'Delete a group', features_base_dir=FEATURES_PATH)
def test_delete_group():
    pass
