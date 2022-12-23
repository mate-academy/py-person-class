class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    persons = []

    for person in people:
        instance_person = Person(name=person["name"], age=person["age"])
        persons.append(instance_person)

    for i in range(len(people)):
        if "wife" in people[i] and people[i]["wife"] is not None:
            persons[i].wife = Person.people[people[i]["wife"]]
        elif "husband" in people[i] and people[i]["husband"] is not None:
            persons[i].husband = Person.people[people[i]["husband"]]
    return persons
