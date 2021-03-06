from model.group import Group
import random

# get lists from db, not ui
def test_delete_some_group(app, db, check_ui):  #add a fixture app as a parameter
    if len(db.get_group_list()) == 0:
       app.group.create(Group(name="test"))

    old_groups = db.get_group_list()  # make a list of groups before deleting a one
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id) # choose group by id, not by index

    # проверки
    assert len(old_groups) - 1 == app.group.count()  # compare size of groups list after deleting a group
    new_groups = db.get_group_list()  # make a list of groups after deleting a one
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui: # only do assertion when --check_ui option exists (it was added as a fixture to conftest.py)
       assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

