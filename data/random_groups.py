from random import randrange, choices
from string import ascii_letters, digits, punctuation
from model.group import Group

def random_string(prefix, maxlen):
    chars = ascii_letters + digits + punctuation + " "*10
    return prefix + "".join(choices(chars, k=randrange(maxlen)))


testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name ", 10), header=random_string("header ", 20), footer=random_string("footer ", 20))
    for i in range(5)
]