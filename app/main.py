class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:

    Person.people = {}
    persons = [Person(person["name"], person["age"]) for person in people]

    for person, data in zip(persons, people):
        if data.get("wife"):
            person.wife = Person.people[data["wife"]]
        elif data.get("husband"):
            person.husband = Person.people[data["husband"]]
    return persons
