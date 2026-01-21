class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people.update({self.name: self})

    @classmethod
    def add_partner(cls, people_list: list) -> None:
        for pers in people_list:
            if "wife" in pers and pers["wife"] is not None:
                cls.people[pers["wife"]].husband = cls.people[pers["name"]]
                cls.people[pers["name"]].wife = cls.people[pers["wife"]]
            elif "husband" in pers and pers["husband"] is not None:
                cls.people[pers["husband"]].wife = cls.people[pers["name"]]
                cls.people[pers["name"]].husband = cls.people[pers["husband"]]


def create_person_list(people: list) -> list:
    result = [Person(human.get("name"), human.get("age")) for human in people]
    Person.add_partner(people)
    return result
