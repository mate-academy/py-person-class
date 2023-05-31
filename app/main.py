class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]
    for person in people:
        unit = Person.people[person["name"]]
        wife = person.get("wife")
        if wife:
            unit.wife = Person.people[wife]
            unit.wife.husband = unit
    return person_list
