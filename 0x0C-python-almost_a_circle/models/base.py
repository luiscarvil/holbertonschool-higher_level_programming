#!/usr/bin/python3
"""
module defines a Base class
"""
import json
import csv


class Base:
    """
    Defines Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ initialization data """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ convert dictionary JSON """
        if list_dictionaries is not None or len(list_dictionaries) != 0:
            return json.dumps(list_dictionaries)
        return []

    @classmethod
    def save_to_file(cls, list_objs):
        """ save dictionary to file """
        filename = cls.__name__ + ".json"
        lista = []
        if list_objs is not None:
            for i in list_objs:
                lista.append(i.to_dictionary())
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(lista))

    @staticmethod
    def from_json_string(json_string):
        """ loads file JSON """
        if json_string is not None or len(json_string) != 0:
            return json.loads(json_string)
        return []

    @classmethod
    def create(cls, **dictionary):
        """ create a dummy by class """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ load files """
        filename = cls.__name__ + ".json"
        lista = []
        try:
            with open(filename, 'r') as f:
                lista = cls.from_json_string(f.read())
            for i, j in enumerate(lista):
                lista[i] = cls.create(**lista[i])
        except Exception:
            pass
        return lista

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ save file format csv """
        filename = cls.__name__ + ".csv"
        lista = [i.to_dictionary() for i in list_objs]
        with open(filename, 'w') as f:
            dictionaries = csv.DictWriter(f, lista[0].keys())
            dictionaries.writeheader()
            dictionaries.writerows(lista)

    @classmethod
    def load_from_file_csv(cls):
        """ load data file from csv """
        filename = cls.__name__ + ".csv"
        lista_d = {}
        lista_c = []
        with open(filename, 'r') as f:
            lista = csv.DictReader(f)
            for i in lista:
                for j, k in dict(i).items():
                    lista_d[j] = int(k)
                lista_c.append(cls.create(**lista_d))
        return lista_c
