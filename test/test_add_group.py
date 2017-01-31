# -*- coding: utf-8 -*-
from model.group import Group

# add db-fixture to get data from db, not from ui
def test_add_group(app, db, json_groups):  # add a fixture app as a parameter, data_groups/json_groups - load data for testing from data/group.py or test.json
    group = json_groups
    old_groups = db.get_group_list() # make a list of groups before adding a new one
    app.group.create(group) # add a new group

    # assert len(old_groups) + 1 == app.group.count()  # compare size of groups list with result of hash-function count()
    new_groups = db.get_group_list()  # make a list of groups after adding a new one
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

