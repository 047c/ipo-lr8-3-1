import json

global counter
counter = 0
status = True


def all_record():
    file = open("dump.json", "r", encoding='utf-8')
    dump = json.load(file)
    print(json.dumps(dump, sort_keys=True, indent=4, ensure_ascii=False))
    file.close()


def all_record_field():
    counter = 0
    file = open("dump.json", "r", encoding='utf-8')
    dump = json.load(file)
    memory_status = False
    find = int(input("Введите значение ID, запись которой нужно вывести: "))
    print(f"{decor}======{decor}")
    for item in dump:
        counter += 1
        if item["id"] == find:
            print(f"ID: {item['id']}")
            print(f"Название звезды: {item['name']}")
            print(f"Название созвездия: {item['constellation']}")
            memory = "Видимая" if item["is_visible"] == "True" else "Не видимая"
            print(f"Видимость без телескопа: {memory}")
            print(f"Радиус: {item['radius']}")
            print(f"Позиция в словаре: {counter}")
            memory_status = True
            break
    if not memory_status:
        print("Запись по вашему ID не найдена!")
    file.close()


def add_record():
    valid = True
    file = open("dump.json", "r", encoding='utf-8')
    dump = json.load(file)
    target_id = -1
    ids = []
    for item in dump:
        ids.append(item['id'])
    for i in range(1, len(ids) + 1):
        if i not in ids:
            target_id = i
            break
    if target_id == -1:
        target_id = len(ids) + 1
    name = input("Введите общее название звезды: ")
    constellation = input("Введите название созвездия: ")
    is_visible = input("Укажите, видима ли звезда без телескопа: (1 - видима, 0 - не видима)")
    radius = (input("Введите радиус: "))
    if is_visible == "1":
        is_visible = True
    elif is_visible == "0":
        is_visible = False
    else:
        valid = False
    new_item = {
        "id": target_id,
        "name": name,
        "constellation": constellation,
        "is_visible": is_visible,
        "radius": radius
    }
    if valid:
        dump.append(new_item)
        print("\nЗапись успешно добавлена!")
    else:
        print("Введите корректное значение видимости звезды.")
    file.close()
    with open("dump.json", "w", encoding='utf-8') as file:
        json.dump(dump, file, indent=4, ensure_ascii=False)


def delete_record():
    memory_status = False
    file = open("dump.json", "r", encoding='utf-8')
    dump = json.load(file)
    find = int(input("Введите значение ID, запись которой нужно удалить: "))
    print(f"{decor}======{decor}")
    for item in dump:
        if item["id"] == find:
            dump.remove(item)
            print(f"Одна запись со значением ID {find} была удалена.")
            memory_status = True
            break
    if not memory_status:
        print(f"Запись со значением ID {find} не найдена.")
    file.close()
    with open("dump.json", "w", encoding='utf-8') as file:
        json.dump(dump, file, indent=4, ensure_ascii=False)


def close_app():
    global status, counter
    print(f"Количество выполненных операций с записями: {counter}")
    print("Выхожу из программы...")
    status = False


def main():
    while status:
        global counter
        print(f"{decor} Меню {decor}")
        print("1 - вывести все записи")
        print("2 - вывести запись по полю")
        print("3 - добавить запись")
        print("4 - удалить запись по полю")
        print("5 - выйти из программы")
        print(f"{decor}======{decor}")
        check = int(input("Введите номер пункта, который нужно выполнить: "))
        print(f"{decor}======{decor}")
        if check == 1:
            all_record()
        elif check == 2:
            all_record_field()
        elif check == 3:
            add_record()
        elif check == 4:
            delete_record()
        elif check == 5:
            close_app()
        else:
            print("Вы ввели некорретное значение!")
            counter -= 1
        counter += 1


decor = "=" * 22
main()