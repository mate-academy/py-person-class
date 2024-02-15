class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


def create_person_list(people: list) -> list:
    person_list = [
        Person(person["name"], person["age"])
        for person in people
    ]

    Person.people = {
        person.name: person
        for person in person_list
    }

    for person in people:
        current_person = Person.people[person["name"]]
        if person.get("wife"):
            current_person.wife = Person.people[person["wife"]]
        if person.get("husband"):
            current_person.husband = Person.people[person["husband"]]
    return person_list
