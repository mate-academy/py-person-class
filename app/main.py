class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for one_person in people:
        person_list.append(Person(one_person["name"], one_person["age"]))
    for i in range(len(people)):
        if "wife" in people[i] and None is not people[i]["wife"]:
            person_list[i].wife = Person.people[people[i]["wife"]]
        if "husband" in people[i] and None is not people[i]["husband"]:
            person_list[i].husband = Person.people[people[i]["husband"]]
    return person_list
