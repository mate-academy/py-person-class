class Person:
    people: dict = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.add_person_to_the_list(self)

    @classmethod
    def add_person_to_the_list(cls, person: object) -> None:
        cls.people[person.name] = person


def create_person_list(people: list) -> list:
    persons: list[Person] = [Person(person["name"], person["age"])
                             for person in people]

    for person in people:
        if "wife" in person and person["wife"] is not None:
            person_to_change = Person.people[person["name"]]
            wife = Person.people[person["wife"]]

            person_to_change.wife = wife
            continue

        if "husband" in person and person["husband"] is not None:
            person_to_change = Person.people[person["name"]]
            husband = Person.people[person["husband"]]

            person_to_change.husband = husband

    return persons
