class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()

    [Person(p["name"], p["age"]) for p in people]
    [setattr(Person.people[p["name"]], "wife",
             Person.people[p["wife"]]) for p in people if p.get("wife")]

    [setattr(Person.people[p["name"]], "husband",
             Person.people[p["husband"]]) for p in people if p.get("husband")]

    return list(Person.people.values())
