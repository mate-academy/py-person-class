class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        person_list.append(Person(person["name"], person["age"]))
    for i in range(len(people)):
        if people[i].get("wife") and people[i]["wife"] is not None:
            person_list[i].wife = Person.people[people[i]["wife"]]
        if people[i].get("husband") and people[i]["husband"] is not None:
            person_list[i].husband = Person.people[people[i]["husband"]]
    return person_list
