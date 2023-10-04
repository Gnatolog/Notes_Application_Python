import json
"""
Класс описывающий функционал приложения

"""

lists_notion = []


class Function:
    def __init__(self):
        self.list = lists_notion

    def save(self):
        """
        Метод сохранения заметок в формате json
        :param self: получает список для записи
        """
        data = {}
        with open('list_note.json', 'w', encoding='utf-8') as sf:

            for i in self.list:
                data[i.get_id()] = ["Title: " + i.get_title(), "Body: " + i.get_body(),"Data: " +  i.get_data()]
            json.dump(data,  sf, ensure_ascii=False)

    def read(self):
        """
        Метод чтения заметок с фильтром по дате
        :param self:  список с заметками не отсортированный
        :return: возвращате остортиованный список  с заметками по дате
        """

        def quicksort(list_sort):
            if len(list_sort) <= 1:
                return list_sort
            else:
                pivot = list_sort[0].get_data()
                left = []
                medium = []
                right = []
                for i in list_sort:
                    if pivot < i.get_data():
                        left.append(i)
                    elif pivot > i.get_data():
                        right.append(i)
                    else:
                        medium.append(i)

                return quicksort(left) + medium + quicksort(right)

        list_notion = quicksort(self.list)
        return list_notion

    def add(self, notie: object):
        """
        Функция добавления заметки в список для хранения
        :param notie: заметка
        :param self: список заметок
        :return: возвращает список с жоваленнвми заметками
        """
        return self.list.append(notie)

    def edit(self, number_id: int, title=None, body=None):
        """
        Метод редактирования замтеки позволяет редактировать загаловок и тело заметки
        :param number_id: Номер заметки
        :param self:  Список заметок
        :param title: Новый загаловок
        :param body:  Новый текс для тела заметки
        :return: Ввозвращает отредоктированный список заметок с учетом времени редоктирования

        """
        for i in self.list:
            if number_id == i.get_id():
                if title is not None and len(title) != 0:
                    i.set_title(title)
                if body is not None and len(body) != 0:
                    i.set_body(body)
                if title is not None or body is not None:
                    i.set_data()
                return self.list
        return None



    def delite(self, number_id: int):
        """
        Метод удалят указанную заметку из списка по id

        :param self: Список заметок
        :param lists_note: Номер заметки который хотим удалить
        :return: Возвращает список заметок удалив при этом указанную заметку
        """
        for i in range(len(self.list)):
            if number_id == self.list[i].get_id():
                return self.list.pop(i)
        return None
