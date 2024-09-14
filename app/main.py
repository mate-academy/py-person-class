class Person:
    people = {}

    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    people_list = [
        Person(element["name"], element["age"]) for element in people
    ]
    for index, human in enumerate(people):
        if "wife" in human and human["wife"] is not None:
            people_list[index].wife = Person.people[human["wife"]]
        elif "husband" in human and human["husband"] is not None:
            people_list[index].husband = Person.people[human["husband"]]

    return people_list
