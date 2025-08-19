class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:

        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(p["name"], p["age"]) for p in people]

    for pep in people:
        person = Person.people[pep["name"]]

        if pep.get("wife"):
            person.wife = Person.people[pep["wife"]]
        if pep.get("husband"):
            person.husband = Person.people[pep["husband"]]

    return person_list
