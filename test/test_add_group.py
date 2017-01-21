# -*- coding: utf-8 -*-
from model.group import Group
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Group(name="", header="", footer="")]+[
    Group(name=random_string("name",10), header=random_string("header",20), footer=random_string("footer",20))
    for i in range(5)
]

@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):  # add a fixture app as a parameter
    old_groups = app.group.get_group_list() # make a list of groups before adding a new one
    app.group.create(group) # add a new group

    assert len(old_groups) + 1 == app.group.count()  # compare size of groups list with result of hash-function count()
    new_groups = app.group.get_group_list()  # make a list of groups after adding a new one
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

