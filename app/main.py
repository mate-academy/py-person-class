class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    persons = [Person(p["name"], p["age"]) for p in people]

    for pers in people:
        person = Person.people[pers["name"]]

        if pers.get("wife"):
            person.wife = Person.people[pers["wife"]]

        if pers.get("husband"):
            person.husband = Person.people[pers["husband"]]

    return persons
