from __future__ import annotations

class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people.update({self.name: self})

    def add_partner_name(self, human: dict) -> None:
        if human.get("wife") != -1 and human.get("wife") is not None:
            self.wife = human.get("wife")
        elif human.get("husband") != -1 and human.get("husband") is not None:
            self.husband = human.get("husband")

    @classmethod
    def add_partner_link(cls, peoples: dict) -> None:

        for human in cls.people:
            if cls.people[human].__dict__.get("wife") is not None:
                cls.people[human].wife = cls.people[cls.people[human].wife]
            elif cls.people[human].__dict__.get("husband") is not None:
                cls.people[human].husband = cls.people[cls.people[human].husband]

def create_person_list(people_list: list) -> list:
    result = [Person(human.get("name"), human.get("age")) for human in people_list]
    for index, human in enumerate(people_list):
        result[index].add_partner_name(people_list[index])
    Person.add_partner_link(people_list)
    print(Person.people)
    return result


people_data = [{'age': 30, 'name': 'Git', 'wife': 'Ross'}, {'age': 29, 'name': 'Joey', 'wife': "Lola"}, {'age': 31, 'husband': "Git", 'name': 'Ross'}, {'age': 31, 'wife': "Joey", 'name': 'Lola'}, {'age': 21, 'wife': None, 'name': 'Rira'}]

create_person_list(people_data)

