class Person:
    people = dict()

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        person_list.append(Person(person["name"], person["age"]))

    for i in people:
        if "wife" in i and i["wife"] is not None:
            Person.people[i["name"]].wife = Person.people[i["wife"]]
        elif "husband" in i and i["husband"] is not None:
            Person.people[i["name"]].husband = Person.people[i["husband"]]

    return person_list
