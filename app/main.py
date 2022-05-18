class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.people[self.name] = self

    @classmethod
    def is_wife(cls, person):
        if "wife" in person and person["wife"] is not None:
            if person["wife"] in cls.people:
                cls.people[person["name"]].wife = cls.people[person["wife"]]
                cls.people[person["wife"]].husband = cls.people[person["name"]]

    @classmethod
    def is_husband(cls, pers):
        if "husband" in pers and pers["husband"] is not None:
            if pers["husband"] in cls.people:
                cls.people[pers["name"]].husband = cls.people[pers["husband"]]
                cls.people[pers["husband"]].wife = cls.people[pers["name"]]


def create_person_list(people: list) -> list:
    for person in people:
        Person(person["name"], person["age"])
        Person.is_wife(person)
        Person.is_husband(person)
    return [Person.people[name] for name in Person.people]
