from model.contact import Contact
import string
import random
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 6
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10 + "-"  # + string.punctuation
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_name(prefix, maxlen):
    symbols = string.ascii_lowercase + string.ascii_uppercase + "-"
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_phone_number(maxlen):
    symbols = string.digits + "-" + " " + "+" + "(" + ")"
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", middlename="", lastname="", nickname="",
                      title="", company="", address="", homephone="", mobilephone="",
                      workphone="", fax_phone="", email="", email2="", email3="")] + [
    Contact(firstname=random_name("firstname", 10), middlename=random_name("middlename", 10),
            lastname=random_name("lastname", 10), nickname=random_name("nickname", 10),
            title=random_name("title", 10), company=random_string("company", 10),
            address=random_string("address", 10), homephone=random_phone_number(10),
            mobilephone=random_phone_number(10), workphone=random_phone_number(10),
            fax_phone=random_phone_number(10), email=random_string("email", 10),
            email2=random_string("email2", 10), email3=random_string("email3", 10))
    for i in range(3)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
print("Путь к файлу:", file)  # можно добавить конфигурацию -n 10 -f data/test.json через Script Parameters

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))

