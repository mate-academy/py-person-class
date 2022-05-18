class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    list_of_people = [
        Person(person['name'], person['age'])
        for person in people
    ]

    for i in range(len(list_of_people)):
        if "wife" in people[i] and people[i]["wife"] is not None:
            list_of_people[i].wife = Person.people[people[i]["wife"]]
        if "husband" in people[i] and people[i]["husband"] is not None:
            list_of_people[i].husband = Person.people[people[i]["husband"]]

    return list_of_people
