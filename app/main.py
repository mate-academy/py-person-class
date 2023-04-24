class Person:

    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:

    info_list = []

    for person in people:
        info_list.append(Person(person["name"], person["age"]))
    for person in people:
        if "wife" in person.keys():
            if person["wife"] is not None:
                man = person["name"]
                wife = person["wife"]
                Person.people[man].wife = Person.people[wife]
        if "husband" in person.keys():
            if person["husband"] is not None:
                woman = person["name"]
                husband = person["husband"]
                Person.people[woman].husband = Person.people[husband]

    return info_list
