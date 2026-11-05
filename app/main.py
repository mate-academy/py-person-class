class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    person_list = [Person(person["name"], person["age"]) for person in people]

    for person, person_data in zip(person_list, people):
        for relation in ("wife", "husband"):
            partner_name = person_data.get(relation)
            if partner_name:
                setattr(person, relation, Person.people[partner_name])

    return person_list
