class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:

    for p in people:
        Person(p["name"], p["age"])

    for p in people:
        inst = Person.people[p["name"]]
        w = p.get("wife")
        if w is not None:
            inst.wife = Person.people.get(w)
        h = p.get("husband")
        if h is not None:
            inst.husband = Person.people.get(h)

    return [Person.people[p["name"]] for p in people]