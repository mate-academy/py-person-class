class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = [
        Person(person_data["name"], person_data["age"])
        for person_data in people
    ]

    for i, person_data in enumerate(people):
        for relationship in ("wife", "husband"):
            spouse_name = person_data.get(relationship)
            if spouse_name:
                setattr(
                    person_list[i], relationship, Person.people[spouse_name]
                )

    return person_list
