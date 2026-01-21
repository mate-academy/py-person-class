class Person:
    people = {}
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = []
    for person in people:
        Person(person["name"], person["age"])
    for person in people:
        if "wife" in person and person["wife"] is not None:
            Person.people[person["wife"]].husband = Person.people[person["name"]]
        if "husband" in person and person["husband"] is not None:
            Person.people[person["husband"]].wife = Person.people[person["name"]]
        result.append(Person.people[person["name"]])
    return result
