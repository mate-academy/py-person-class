class Person:

    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    ls = [Person(pers["name"], pers["age"])for pers in people]
    for i in range(len(ls)):
        if "wife" in people[i] and people[i]["wife"] is not None:
            ls[i].wife = Person.people[people[i]["wife"]]
        if "husband" in people[i] and people[i]["husband"] is not None:
            ls[i].husband = Person.people[people[i]["husband"]]
    return ls
