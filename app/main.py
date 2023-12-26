from __future__ import annotations

class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people.update({self.name: self})

    @classmethod
    def add_partner(cls, peoples: list) -> None:
        for human in peoples:
            if human.get("wife") != -1 and human.get("wife") is not None:
                if human.get("wife") in cls.people:
                    cls.people[human["name"]].wife = cls.people[human["wife"]]
                    cls.people[human["wife"]].husband = cls.people[human["name"]]
            elif human.get("husband") != -1 and human.get("husband") is not None:
                if human.get("husband") in cls.people:
                    cls.people[human["name"]].husband = cls.people[human["husband"]]
                    cls.people[human["husband"]].wife = cls.people[human["name"]]


def create_person_list(people_list: list) -> list:
    result = [Person(human.get("name"), human.get("age")) for human in people_list]
    Person.add_partner(people_list)
    print(Person.people)
    return result




