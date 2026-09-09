class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    mas = []
    for i in people:
        mass = Person(i["name"], i["age"])
        mas.append(mass)
    for i in people:
        memi = i.get("wife")
        if memi is not None:
            Person.people[i["name"]].wife = Person.people[memi]
        mem = i.get("husband")
        if mem is not None:
            Person.people[i["name"]].husband = Person.people[mem]
    return mas
