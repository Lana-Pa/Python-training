from model.group import Group
import random

def test_modify_group_name(app, db, check_ui):  #add a fixture app as a parameter
    if db.get_group_list() == 0:
       app.group.create(Group(name="My group"))

    old_groups = db.get_group_list()   # make a list of groups before modifying
    group = random.choice(old_groups)
    app.group.modify_group_by_id(group.id, group)  # choose group by id, not by index

    # проверки
    assert len(old_groups) ==  app.group.count()  # compare size of groups list after modifying - it should be equal
    new_groups = db.get_group_list()  # make a list of groups after modifying
    assert old_groups == new_groups
    if check_ui: # only do assertion when --check_ui option exists (it was added as a fixture to conftest.py)
       assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
