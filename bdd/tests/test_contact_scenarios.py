from pytest_bdd import scenario
from bdd.steps.contact_steps import *

FEATURES_PATH = '../features'


@scenario('contacts.feature', 'Add new contact', features_base_dir=FEATURES_PATH)
def test_add_contact():
    pass


@scenario('contacts.feature', 'Delete contact', features_base_dir=FEATURES_PATH)
def test_delete_contact():
    pass


@scenario('contacts.feature', 'Modify contact', features_base_dir=FEATURES_PATH)
def test_modify_contact():
    pass
