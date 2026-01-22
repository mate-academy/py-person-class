class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    for person in people:
        name = person["name"]
        age = person["age"]
        Person(name, age)

    for peopl in people:
        peep = Person.people[peopl["name"]]
        if "wife" in peopl and peopl["wife"] is not None:
            peep.wife = Person.people[peopl["wife"]]
        if "husband" in peopl and peopl["husband"] is not None:
            peep.husband = Person.people[peopl["husband"]]
        else:
            peep.husband = None

    return [Person.people[person["name"]] for person in people]
