class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[name] = self


def create_person_list(people: list) -> list:
    new_list = []
    for person in people:
        new_list.append(Person(name=person["name"], age=person["age"]))
    for index, person in enumerate(people):
        if "wife" in person and person["wife"] is not None:
            new_list[index].wife = Person.people[person["wife"]]
        if "husband" in person and person["husband"] is not None:
            new_list[index].husband = Person.people[person["husband"]]

    return new_list
