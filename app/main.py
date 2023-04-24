class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.__class__.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        person_list.append(Person(person["name"], person["age"]))
    for i, person in enumerate(people):
        if "wife" in dict.keys(person) and person["wife"] is not None:
            person_list[i].wife = Person.people[person["wife"]]
        if "husband" in dict.keys(person) and person["husband"] is not None:
            person_list[i].husband = Person.people[person["husband"]]

    return person_list
