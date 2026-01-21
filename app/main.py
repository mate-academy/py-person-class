class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = []
    for person in people:
        result.append(Person(person["name"], person["age"]))

    for p in people:
        if "wife" in p.keys() and p["wife"] is not None:
            Person.people[p["name"]].wife = Person.people[p["wife"]]
        elif "husband" in p.keys() and p["husband"] is not None:
            Person.people[p["name"]].husband = Person.people[p["husband"]]
    return result
