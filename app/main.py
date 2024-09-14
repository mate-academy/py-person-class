class Person:
    people = {}

    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    people_list = []
    for element in people:
        people_list.append(Person(element["name"], element["age"]))

    for i, element in enumerate(people):
        if "wife" in element and element["wife"] is not None:
            people_list[i].wife = Person.people[element["wife"]]
        elif "husband" in element and element["husband"] is not None:
            people_list[i].husband = Person.people[element["husband"]]

    return people_list
