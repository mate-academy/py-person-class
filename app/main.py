class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    for person in people:
        Person(person["name"], person["age"])
    for j in people:
        if "wife" in j:
            if not j["wife"] is None:
                Person.people[j["name"]].wife = Person.people[j["wife"]]
            else:
                Person.people[j["name"]].wife = None
        if "husband" in j:
            if not j["husband"] is None:
                Person.people[j["name"]].husband = Person.people[j["husband"]]
            else:
                Person.people[j["name"]].husband = None
    return list(Person.people.values())


