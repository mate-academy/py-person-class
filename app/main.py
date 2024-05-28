class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    people_list = [Person(
        person["name"],
        person["age"])
        for person in people]

    for i, person in enumerate(people):
        if people[i].get("wife"):
            people_list[i].wife = Person.people[people[i]["wife"]]
        if people[i].get("husband"):
            people_list[i].husband = Person.people[people[i]["husband"]]
    return people_list
