class Person:
    people: dict = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.__class__.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}
    instances = []
    for p in people:
        inst = Person(p["name"], p["age"])
        instances.append(inst)

    for p in people:
        inst = Person.people[p["name"]]
        if "wife" in p and p["wife"] is not None:
            inst.wife = Person.people.get(p["wife"])
        if "husband" in p and p["husband"] is not None:
            inst.husband = Person.people.get(p["husband"])
    return instances
