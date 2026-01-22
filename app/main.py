class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        person_list.append(Person(name=person["name"], age=person["age"]))
    for i, person in enumerate(people):
        if person.get("wife") is not None:
            person_list[i].wife = Person.people[person["wife"]]
        elif person.get("husband") is not None:
            person_list[i].husband = Person.people[person["husband"]]
    return person_list
