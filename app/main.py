class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    persons = [Person(person["name"], person["age"]) for person in people]
    for person_data, person in zip(people, persons):
        for relationship in ("wife", "husband"):
            partner_name = person_data.get(relationship)
            if partner_name is not None:
                setattr(person, relationship, Person.people[partner_name])
    return persons
