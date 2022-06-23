class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    persons_list = []
    for person in people:
        persons_list.append(Person(person["name"], person["age"]))
    for i in range(len(people)):
        if "wife" in people[i] and people[i]["wife"] is not None:
            persons_list[i].wife = Person.people[people[i]["wife"]]
        if "husband" in people[i] and people[i]["husband"] is not None:
            persons_list[i].husband = Person.people[people[i]["husband"]]
    return persons_list
