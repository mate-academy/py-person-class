class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__class__.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        new_person = Person(person["name"], person["age"])
        person_list.append(new_person)

    for person in people:
        if "husband" in person and person["husband"] is not None:
            Person.people[person["name"]].husband = \
                Person.people[person["husband"]]

        if "wife" in person and person["wife"] is not None:
            Person.people[person["name"]].wife = Person.people[person["wife"]]

    return person_list
