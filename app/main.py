class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person = []
    for info_pers in people:
        person.append(Person(
            name=info_pers["name"],
            age=info_pers["age"],
        ))
    for info_pers in people:
        if "wife" in info_pers and info_pers["wife"] is not None:
            Person.people[info_pers["name"]].wife = \
                Person.people[info_pers["wife"]]
        elif "husband" in info_pers and info_pers["husband"] is not None:
            Person.people[info_pers["name"]].husband = \
                Person.people[info_pers["husband"]]
    return person
