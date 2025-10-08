class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:

        self.name = name
        self.age = age
        Person.people[name] = self
    pass


def create_person_list(people: list[dict]) -> list:

    person_list = []
    for person in people:
        person_list.append(Person(person["name"], person["age"]))

    for person in people:
        current = Person.people[person["name"]]
        rel_key = "wife" if "wife" in person else "husband"
        partner_name = person.get(rel_key)

        if partner_name is not None:
            partner = Person.people[partner_name]
            setattr(current, rel_key, partner)
            if not hasattr(
                    partner, "husband" if rel_key == "wife" else "wife"):
                rev = "husband" if rel_key == "wife" else "wife"
                setattr(partner, rev, current)
    return person_list

    pass
