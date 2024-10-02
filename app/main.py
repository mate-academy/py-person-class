class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self

    def set_partner(self, partner: "Person") -> None:
        if "husband" in partner.__dict__:
            self.husband = partner
            partner.wife = self
        else:
            self.wife = partner
            partner.husband = self


def create_person_list(people: list[dict]) -> list["Person"]:
    person_instances = {}

    for person_data in people:
        name = person_data["name"]
        age = person_data["age"]

        person_instance = Person(name, age)
        person_instances[name] = person_instance

    for person_data in people:
        name = person_data["name"]
        partner_key = "wife" if "wife" in person_data else "husband"
        partner_name = person_data.get(partner_key)

        if partner_name:
            partner_instance = person_instances[partner_name]
            person_instances[name].set_partner(partner_instance)

    return list(person_instances.values())
