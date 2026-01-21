class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    person_list = [
        Person(person["name"], person["age"]) for person in people
    ]

    for person in people:
        current_person = Person.people.get(person["name"])
        if not current_person:
            continue
        if "wife" in person and person["wife"] in Person.people:
            current_person.wife = Person.people[person["wife"]]
        elif "husband" in person and person["husband"] in Person.people:
            current_person.husband = Person.people[person["husband"]]

    return person_list
