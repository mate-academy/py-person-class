class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list["Person"]:

    person_instances = {
        person_data["name"]: Person(person_data["name"], person_data["age"])
        for person_data in people
    }

    for person_data in people:
        name = person_data["name"]
        partner_key = "wife" if "wife" in person_data else "husband"
        partner_name = person_data.get(partner_key)
        if partner_name:
            partner_instance = person_instances[partner_name]
            setattr(person_instances[name], partner_key, partner_instance)
            setattr(
                partner_instance,
                "husband" if partner_key == "wife" else "wife",
                person_instances[name]
            )

    return list(person_instances.values())
