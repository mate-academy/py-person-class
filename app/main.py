class Person:

    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:

    people_list = []

    for each in people:
        person = Person(each["name"], each["age"])
        people_list.append(person)

    for i in range(len(people)):
        if "wife" in people[i] and people[i]["wife"] is not None:
            people_list[i].wife = Person.people[people[i]["wife"]]
        if "husband" in people[i] and people[i]["husband"] is not None:
            people_list[i].husband = Person.people[people[i]["husband"]]

    return people_list
