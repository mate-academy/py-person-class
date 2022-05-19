class Person:

    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = [Person(person["name"], person["age"]) for person in people]

    for person in range(len(people)):
        if "wife" in people[person] and people[person]["wife"]:
            result[person].wife = Person.people[people[person]["wife"]]
        if "husband" in people[person] and people[person]["husband"]:
            result[person].husband = Person.people[people[person]["husband"]]

    return result
