class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people.update({self.name: self})


def create_person_list(people: list) -> list:
    person_list = []
    for dct in people:
        person_list.append(Person(dct["name"], int(dct["age"])))
    for dct in people:
        if "husband" in dct and dct["husband"] is not None:
            Person.people[dct["name"]].husband \
                = Person.people[dct["husband"]]
        if "wife" in dct and dct["wife"] is not None:
            Person.people[dct["name"]].wife = Person.people[dct["wife"]]
    return person_list
