class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:

        self.name = name
        self.age = age
        Person.people[name] = self
    pass


def create_person_list(people: list[dict]) -> list[Person]:

    person_list = []
    person_list = [Person(p.get("name"), p.get("age")) for p in people]

    for person in people:
        current = Person.people[person["name"]]
        rel_key = "wife" if person.get("wife") else "husband"
        partner_name = person.get(rel_key)

        if partner_name is not None:
            partner = Person.people[partner_name]
            setattr(current, rel_key, partner)

            reverse_key = "husband" if rel_key == "wife" else "wife"
            partner_dict = next(
                (p for p in people if p["name"] == partner_name), None)

            if partner_dict and partner_dict.get(reverse_key) == current.name:
                setattr(partner, reverse_key, current)

        return person_list

    pass
