from random import randrange, choices
from string import ascii_letters, digits, punctuation
from model.contact import Contact
from os.path import abspath, dirname, join
import jsonpickle
import getopt
import sys


num_of_contacts = 3
result_file = "data/random_contacts.json"

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:",
                               ["number of contacts to generate",
                                "output filename related to project root directory"])
except getopt.GetoptError as err:
    # print help information and exit:
    print(err)
    getopt.usage()
    sys.exit(2)

for opt, val in opts:
    if opt == "-n":
        num_of_contacts = int(val)
    elif opt == "-f":
        result_file = val


def random_string(prefix, maxlen):
    chars = ascii_letters + digits + punctuation + " "*10
    return prefix + "".join(choices(chars, k=randrange(maxlen)))


test_data = [
    Contact(firstname=random_string("first", 10), lastname=random_string("last", 10), mobile=random_string("", 10))
    for i in range(num_of_contacts)
]

file = join(dirname(abspath(__file__)), "..", result_file)

with open(file, "w") as f:
    jsonpickle.set_encoder_options("json", indent=2)
    f.write(jsonpickle.encode(test_data))