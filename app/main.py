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

        if "husband" in person and person["husband"]:
            name = Person(person["name"], person["age"])
            name.husband = person["husband"]
        else:
            name = Person(person["name"], person["age"])
        person_list.append(name)
    for person in people:
        human = Person.people[person["name"]]
        if "wife" in person and person["wife"]:
            human.wife = Person.people[person["wife"]]
        if "husband" in person and person["husband"]:
            human.husband = Person.people[person["husband"]]
    return person_list
