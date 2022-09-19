class Person:
    people = {}

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    for person in people:
        Person(person["name"], person["age"])

    for index, name in enumerate(Person.people):
        if "wife" in people[index] and people[index]["wife"] is None:
            continue
        elif "husband" in people[index] and people[index]["husband"] is None:
            continue

        if "wife" in people[index]:
            Person.people[name].wife = Person.people[people[index]["wife"]]
        elif "husband" in people[index]:
            Person.people[name].husband = \
                Person.people[people[index]["husband"]]

    return list(Person.people.values())
