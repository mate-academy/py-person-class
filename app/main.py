class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person = []
    for data in people:
        person.append(Person(
            name=data["name"],
            age=data["age"],
        ))
    for data in people:
        if "wife" in data and data["wife"] is not None:
            Person.people[data["name"]].wife = Person.people[data["wife"]]
        elif "husband" in data and data["husband"] is not None:
            Person.people[data["name"]].husband = \
                Person.people[data["husband"]]
    return person
