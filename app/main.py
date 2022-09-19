class Person:

    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        person_list.append(Person(person["name"], person["age"]))
    for index, person in enumerate(people):
        if "wife" in person:
            if person["wife"] is None:
                continue
            person_list[index].wife = Person.people[person["wife"]]
        else:
            if person["husband"] is None:
                continue
            person_list[index].husband = Person.people[person["husband"]]
    return person_list
