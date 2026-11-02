class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    persons = [Person(person["name"], person["age"]) for person in people]
    for person, details in zip(persons, people):
        if details.get("wife") is not None:
            person.wife = Person.people[details["wife"]]
        if details.get("husband") is not None:
            person.husband = Person.people[details["husband"]]
    return persons
