from datetime import datetime
import itertools

"""
Класс описывающий заметку

"""


class Note:
    __id_generation = itertools.count(1)  # создает уникальный id начиная с 1

    # region constructor

    def __init__(self, title: str, body: str):
        self.__id_note = next(self.__id_generation)  # уникальный id заметки
        self.__title = title  # загаловок заметки
        self.__body = body  # тело заметки
        self.__data = datetime.now()  # дата создания заметки

    # endregion

    # region method
    def __str__(self):
        """
        Переорпрелеение метода  print string
        :return: Возвращает отформатированую заметку

        """
        result = f"Id заметки: {self.__id_note} \n" \
                 f"Дата созадание заметки: {self.__data.strftime('%H:%M:%S %d/%m/%Y')}\n" \
                 f"Загаловок заметки: {self.__title}\n" \
                 f"Тело заметки: {self.__body}\n"

        return result
    # endregion

    # region Getter and Setter

    def get_id(self):
        return self.__id_note

    def get_title(self):
        return self.__title

    def get_body(self):
        return self.__body

    def get_data(self):
        current_time = self.__data.strftime("%H:%M:%S %d/%m/%Y")
        return current_time

    def set_title(self, title: str):
        self.__title = title
        return self.__title

    def set_body(self, body: str):
        self.__body = body
        return self.__body

    def set_data(self):
        self.__data = datetime.now()

    # endregion
