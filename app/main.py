class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]
    for i in range(len(people)):
        if "wife" in people[i].keys():
            if people[i]["wife"]:
                person_list[i].wife = Person.people[people[i]["wife"]]
        if "husband" in people[i].keys():
            if people[i]["husband"]:
                person_list[i].husband = Person.people[people[i]["husband"]]

    return person_list
