class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]

    for person_data, person in zip(people, person_list):
        for relationship in ("wife", "husband"):
            related_name = person_data.get(relationship)
            if related_name is not None:
                setattr(person, relationship, Person.people[related_name])

    return person_list
