class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    person_instances_list = []

    for index in range(len(people)):
        person = Person(people[index]["name"], people[index]["age"])
        person_instances_list.append(person)
    for index in range(len(people)):
        if "wife" in people[index] and people[index]["wife"] is not None:
            Person.people[people[index]["name"]].wife = \
                Person.people[people[index]["wife"]]
        if "husband" in people[index] and people[index]["husband"] is not None:
            Person.people[people[index]["name"]].husband = \
                Person.people[people[index]["husband"]]
    return person_instances_list
