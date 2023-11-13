class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people.update({self.name: self})


def create_person_list(people: list) -> list:
    result = [Person(person["name"], person["age"]) for person in people]
    for partner in people:
        name = partner["name"]
        if "wife" in partner and partner["wife"] is not None:
            Person.people[name].wife = Person.people[partner["wife"]]
        elif "husband" in partner and partner["husband"] is not None:
            Person.people[name].husband = Person.people[partner["husband"]]
    return result
