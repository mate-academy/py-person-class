class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    for i in people:
        Person(i["name"], i["age"])
    for i in range(len(people)):
        if "wife" in people[i]:
            if people[i]["wife"] is not None:
                setattr(Person.people[people[i]["name"]], "wife",
                        Person.people[people[i]["wife"]])
        if "husband" in people[i]:
            if people[i]["husband"] is not None:
                setattr(Person.people[people[i]["name"]], "husband",
                        Person.people[people[i]["husband"]])
    return [i for i in Person.people.values()]
