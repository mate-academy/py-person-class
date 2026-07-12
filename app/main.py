class Person:
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    persons = [Person(person["name"], person["age"]) for person in people]

    for person, data in zip(persons, people):
        for relation in ("wife", "husband"):
            partner_name = data.get(relation)
            if partner_name is not None:
                setattr(person, relation, Person.people[partner_name])

    return persons
