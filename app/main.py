class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}

    person_list = []
    for data in people:
        person_list.append(Person(data["name"], data["age"]))

    for data in people:
        name = data["name"]
        if "wife" in data and data["wife"] is not None:
            Person.people[name].wife = Person.people[data["wife"]]
        if "husband" in data and data["husband"] is not None:
            Person.people[name].husband = Person.people[data["husband"]]

    return person_list
