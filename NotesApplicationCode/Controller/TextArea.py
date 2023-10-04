def change_print_text(comand):
    match comand:

        case "not_found":
            text = "Заметка не найдена"
            print(text)

        case "warning":
            text = """\
    Не желаете сохранить данные перед выходом  если хотите сохранить нажмите Y " 
    иначе изменения сохраненны не будут: 
                   """
            answer = input(text)
            return answer

        case "error":
            print("Вы ввели некоректное значение повторите ввод")

        case "note_del":
            text = "Введите номер заметки которую хотите удалить: "
            id_note = input(text)
            return id_note

        case "note_edit":
            text = "Введите номер заметки которую хотите отредактировать: "
            id_note = input(text)
            return id_note
        case "body":
            text = "Введите что желаете сохранить в Заметки: "
            body = input(text)
            return body

        case "title":
            text = "Введите Заголовок Заметки: "
            title = input(text)
            return title

        case "action":
            text = "Выберите значения от 1 до 6: "
            action = input(text)
            return action

        case "choice":
            print("Доступные действия".upper() + "\n")

        case "save":
            text = "Заметки успешно сохранены"
            print_star(text)

        case "read":
            text = "Чтение заметок завершено"
            print_star(text)
        case "add":
            text = "Заметка успешно добавлена"
            print_star(text)

        case "edit":
            text = "Заметка успешно изменена"
            print_star(text)

        case "del":
            text = "Заметка успешно удалена"
            print_star(text)

        case "start":
            text = "Добро пожаловать в консольное приложение Заметки"
            ptint_title(text)

        case "exit":
            text = "До свидания"
            ptint_title(text)
        case "not":
            print("Список заметок пуст")
        case "menu":
            menu = ['Сохранить заметку', 'Посмотреть заметки',
                    'Добавить заметку', 'Отредактировать заметку',
                    'Удалить заметку', 'Выйти из приложения']
            for i in range(len(menu)):
                print(i + 1, menu[i], "\n")


def print_star(text):
    """
    Функция печати звезд над и под текстом
    :param text: Как текст выводим
    """

    star = ""
    for i in range(len(text)):
        star = "*" * (len(text))
    print("\t", star, "\n")
    print("\t", text + "\n")
    print("\t", star, "\n")


def ptint_title(text):
    """
    Функция печати звезд над и под текстом главных меню
    :param text: Как текст выводим
    """
    star = ""
    for i in range(len(text)):
        star = "*" * (len(text) + 8)
    print("\t", star)
    print("\n\t\t", text.upper() + "\n")
    print("\t", star, "\n")



