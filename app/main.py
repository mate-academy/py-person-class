class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person = []
    for key in people:
        person.append(Person(
            name=key["name"],
            age=key["age"],
        ))
    for key in people:
        if "wife" in key and key["wife"] is not None:
            Person.people[key["name"]].wife = Person.people[key["wife"]]
        elif "husband" in key and key["husband"] is not None:
            Person.people[key["name"]].husband = Person.people[key["husband"]]
    return person
