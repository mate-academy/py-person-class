class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    persons = []
    for pers in people:
        persons.append(Person(pers["name"], pers["age"]))
    for pers in people:
        if pers.get("husband") is not None:
            Person.people[pers["name"]].husband = \
                Person.people[pers["husband"]]
        if pers.get("wife") is not None:
            Person.people[pers["name"]].wife = Person.people[pers["wife"]]
    return persons
