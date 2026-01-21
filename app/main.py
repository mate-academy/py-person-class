class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    Person.people = {}
    persons_list = [Person(person_dict.get("name"),
                    person_dict.get("age")) for person_dict
                    in people if person_dict.get("name") is not None
                    and person_dict.get("age") is not None]

    for person_dict in people:
        current_person = Person.people.get(person_dict.get("name"))
        if not current_person:
            continue
        for relation in ("wife", "husband"):
            partner_name = person_dict.get(relation)
            partner = Person.people.get(partner_name)
            if partner:
                setattr(current_person, relation, partner)

    return persons_list
