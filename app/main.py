class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        person_list.append(Person(person["name"], person["age"]))
    for pair in people:
        if "wife" in pair and pair["wife"] is not None:
            Person.people[pair["name"]].wife = Person.people[pair["wife"]]
        if "husband" in pair and pair["husband"] is not None:
            Person.people[pair["name"]].husband = (
                Person.people[pair["husband"]]
            )

    return person_list
