class Person:
    people = {}

    def __init__(self, person: dict) -> None:
        self.name = person["name"]
        self.age = person["age"]

        self.wife = None
        self.husband = None

        if "wife" in person:
            self.wife = person["wife"]

        if "husband" in person:
            self.husband = person["husband"]

        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    for person in people:
        Person(person)

    for person in Person.people.values():
        if person.wife is not None:
            person.wife = Person.people[person.wife]

        if person.husband is not None:
            person.husband = Person.people[person.husband]
