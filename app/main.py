class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    persons_list = [Person(p["name"], p["age"]) for p in people]

    for i in range(len(people)):
        if people[i].get("wife"):
            persons_list[i].wife = Person.people[people[i]["wife"]]
        if people[i].get("husband"):
            persons_list[i].husband = Person.people[people[i]["husband"]]

    return persons_list
