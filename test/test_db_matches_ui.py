from model.group import Group

def test_group_list(app, db):  # передаем две фикстуры (доступ к ui и db) в качестве параметров
    ui_list = app.group.get_group_list()
    def clean(group):
        return Group(id=group.id, name=group.name.strip()) # удаление лишних пробелов из записей БД

    db_list = map(clean, db.get_group_list())
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)


