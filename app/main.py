class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    person_instances = [
        Person(p["name"], p["age"]) for p in people
    ]

    for person_dict in people:
        person_obj = Person.people[person_dict["name"]]
        for relation in ["wife", "husband"]:
            partner_name = person_dict.get(relation)
            if partner_name:
                setattr(person_obj, relation, Person.people[partner_name])

    return person_instances
