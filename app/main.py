class Person:
    people = {}

    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age


def create_person_list(people: list) -> list:

    Person.people = {}
    person_list = {pers["name"]: Person(pers["name"],
                                        pers["age"]) for pers in people}

    for pers in people:
        persons = person_list[pers["name"]]
        if "wife" in pers and pers["wife"] is not None:
            persons.wife = person_list[pers["wife"]]
        if "husband" in pers and pers["husband"] is not None:
            persons.husband = person_list[pers["husband"]]

    Person.people = person_list

    return list(person_list.values())
