class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_instances = []

    for person_data in people:
        name = person_data["name"]
        age = person_data["age"]
        person_instances.append(Person(name, age))

    for person_data in people:
        name = person_data["name"]
        if "wife" in person_data and person_data["wife"] is not None:
            Person.people[name].wife = Person.people[person_data["wife"]]
        if "husband" in person_data and person_data["husband"] is not None:
            Person.people[name].husband = Person.people[person_data["husband"]]

    return list(Person.people.values())
