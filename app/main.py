class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    slov = {
        i["name"]: Person(i["name"], i["age"])
        for i in people
    }
    for i in people:
        if i.get("wife"):
            slov[i["name"]].wife = Person.people[i["wife"]]
        elif i.get("husband"):
            slov[i["name"]].husband = Person.people[i["husband"]]
    return list(slov.values())
