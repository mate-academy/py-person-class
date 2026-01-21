class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people.update({self.name: self})


def create_person_list(people1: list) -> list:
    output_list = [Person(pers["name"], pers["age"]) for pers in people1]

    for i in range(len(people1)):
        if "wife" in people1[i] and people1[i]["wife"] is not None:
            output_list[i].wife = Person.people[people1[i]["wife"]]
        elif "husband" in people1[i] and people1[i]["husband"] is not None:
            output_list[i].husband = Person.people[people1[i]["husband"]]

    return output_list
