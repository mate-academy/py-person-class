class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        if "wife" in person and person["wife"]:
            name = Person(person["name"], person["age"])
            name.wife = person["wife"]
            person_list.append(name)
            continue
        if "husband" in person and person["husband"]:
            name = Person(person["name"], person["age"])
            name.husband = person["husband"]
            person_list.append(name)
            continue
        else:
            name = Person(person["name"], person["age"])
            person_list.append(name)
    for person in people:
        persona = Person.people[person["name"]]
        if "wife" in person and person["wife"]:
            persona.wife = Person.people[person["wife"]]
        if "husband" in person and person["husband"]:
            persona.husband = Person.people[person["husband"]]
    return person_list
