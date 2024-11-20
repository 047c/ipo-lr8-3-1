import json

decor = "=" * 22
status = True
counter = 0
while status:
    memory_status = False
    status = True
    file = open("dump.json", "r", encoding='utf-8')
    dump = json.load(file)
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
        print(json.dumps(dump, sort_keys=True, indent=4, ensure_ascii=False))
    elif check == 2:
        find = int(input("Введите значение ID, запись которой нужно вывести: "))
        print(f"{decor}======{decor}")
        for item in dump:
            if item["id"] == find:
                print(f"ID: {item['id']}")
                print(f"Название звезды: {item['name']}")
                print(f"Название созвездия: {item['constellation']}")
                memory = "Видимая" if item["is_visible"] == "True" else "Не видимая"
                print(f"Видимость без телескопа: {memory}")
                print(f"Радиус: {item['radius']}")
                memory_status = True
                break
        if not memory_status:
            print("/nЗапись по вашему ID не найдена!")
    elif check == 3:
        id_d = int(input("Введите значение ID предмета: "))
        name = input("Введите общее название звезды: ")
        constellation = input("Введите название созвездия: ")
        is_visible = input("Укажите, видима ли звезда без телескопа: (1 - видима, 0 - не видима)")
        radius = input("Введите радус: ")
        is_visible = "True" if is_visible == "1" else "False"
        new_item = {
            "id": id_d,
            "name": name,
            "constellation": constellation,
            "is_visible": is_visible,
            "radius": radius
        }
        dump.append(new_item)
        print("\nЗапись успешно добавлена!")
    elif check == 4:
        find = int(input("Введите значение ID, запись которой нужно удалить: "))
        print(f"{decor}======{decor}")
        for item in dump:
            if item["id"] == find:
                dump.remove(item)
                print(f"Одна запись со значением ID {find} была удалена.")
                memory_status = True
                break
        if not memory_status:
            print(f"\nЗапись со значением ID {find} не найдена.")
    elif check == 5:
        print(f"Количество выполненных операций с записями: {counter}")
        print("Выхожу из программы...")
        status = False
    else:
        print("Вы ввели некорретное значение!")
        counter -= 1
    file.close()
    counter += 1
    with open("dump.json", "w", encoding='utf-8') as file:
        json.dump(dump, file, indent=4, ensure_ascii=False)
    check = 0