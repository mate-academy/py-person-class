class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(persons: list) -> list:

    person_list = [Person(person["name"], person["age"]) for person in persons]

    for person in persons:
        marital = "wife" if "wife" in person else "husband"
        if person[marital] is not None:
            setattr(
                Person.people[person["name"]],
                marital,
                Person.people[person[marital]]
            )

    return person_list
