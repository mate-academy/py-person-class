class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result = [Person(person.get('name'), person.get('age'))for person in people]

    for person in people:
        spouse = Person.people[person.get('name')]
        if person.get("wife"):
            spouse.wife = Person.people[person.get('wife')]
        if person.get("husband"):
            spouse.husband = Person.people[person.get('husband')]

    return result
