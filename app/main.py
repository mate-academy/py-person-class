class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list[Person]:
    person_list = [
        Person(person["name"], person["age"]) for person in people
    ]

    for person in people:
        p = Person.people.get(person["name"])
        if person.get("wife"):
            p.wife = Person.people.get(person["wife"])
        if person.get("husband"):
            p.husband = Person.people.get(person["husband"])

    return person_list
