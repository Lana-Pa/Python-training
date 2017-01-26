from model.contact import Contact
import random
import string
import os.path
import json
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    # print help information and exit:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o,a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

# generate test data
testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company="",
                    address="", home_phone="", mobile_phone="",work_phone="", email1="",email2="", email3="",
                    homepage="", address2="", phone2="")]+[
            Contact(firstname=random_string("firstname",10), middlename=random_string("middlename",10),
                    lastname=random_string("lastname",10), nickname=random_string("nickname",10),
                    title=random_string("title",10), company=random_string("company",10),
                    address=random_string("address",15), home_phone=random_string("homephone",10),
                    mobile_phone=random_string("mobilephone",10),work_phone=random_string("workphone",10),
                    email1=random_string("email1",10),email2=random_string("email2",10),
                    email3=random_string("email3",10), homepage=random_string("homepage",10), address2=random_string("address2",10),
                    phone2=random_string("phone2",10))
            for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file,"w") as out:
    out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))
