from random import randrange, choices
from string import ascii_letters, digits, punctuation
from model.group import Group
from os.path import abspath, dirname, join
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    # print help information and exit:
    print(err)
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/groups.json"

for opt, val in opts:
    if opt == "-n":
        n = int(val)
    elif opt == "-f":
        f = val

def random_string(prefix, maxlen):
    chars = ascii_letters + digits + punctuation + " "*10
    return prefix + "".join(choices(chars, k=randrange(maxlen)))


testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name ", 10), header=random_string("header ", 20), footer=random_string("footer ", 20))
    for i in range(n)
]

file = join(dirname(abspath(__file__)), "..", f)

with open(file, 'w') as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
