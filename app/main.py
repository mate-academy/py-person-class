class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for i in range(len(people)):
        name = people[i].get("name")
        age = people[i].get("age")
        person_list.append(Person(name, age))
    for i in range(len(people)):
        if people[i].get("husband") is not None:
            Person.people[people[i]["name"]].husband \
                = Person.people[people[i]["husband"]]
        if people[i].get("wife") is not None:
            Person.people[people[i]["name"]].wife \
                = Person.people[people[i]["wife"]]
    return person_list
