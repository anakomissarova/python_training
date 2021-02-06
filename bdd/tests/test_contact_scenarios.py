from pytest_bdd import scenario
import os.path
from bdd.steps.contact_steps import *

FEATURES_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../features")


@scenario('contacts.feature', 'Add new contact', features_base_dir=FEATURES_PATH)
def test_add_contact():
    pass


@scenario('contacts.feature', 'Delete contact', features_base_dir=FEATURES_PATH)
def test_delete_contact():
    pass


@scenario('contacts.feature', 'Modify contact', features_base_dir=FEATURES_PATH)
def test_modify_contact():
    pass
