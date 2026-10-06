class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    slov = {}
    for i in people:
        slov[i["name"]] = Person(i["name"], i["age"])
    for i in people:
        if "wife" in i and i["wife"] is not None:
            slov[i["name"]].wife = Person.people[i["wife"]]
        elif "husband" in i and i["husband"] is not None:
            slov[i["name"]].husband = Person.people[i["husband"]]
    return list(slov.values())
