class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    persons = []

    for pers in people:
        person = Person(pers["name"], pers["age"])
        persons.append(person)

    for pers in people:
        person = Person.people[pers["name"]]

        if "wife" in pers and pers["wife"] is not None:
            person.wife = Person.people[pers["wife"]]

        if "husband" in pers and pers["husband"] is not None:
            person.husband = Person.people[pers["husband"]]

    return persons
