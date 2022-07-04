class Person:

    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    persons = []
    for man in people:
        person = Person(man['name'], man['age'])
        persons.append(person)
    for man in people:
        if man.get("wife"):
            Person.people[man["name"]].wife = Person.people[man["wife"]]
        if man.get("husband"):
            Person.people[man["name"]].husband = Person.people[man["husband"]]
    return persons
