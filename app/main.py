class Person:
    people = {}

    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = [Person(person["name"], person["age"]) for person in people]
    i = 0
    for person in people:
        if "wife" in person and person["wife"] is not None:
            result[i].wife = Person.people[person["wife"]]
        if "husband" in person and person["husband"] is not None:
            result[i].husband = Person.people[person["husband"]]
        i += 1
    return result
