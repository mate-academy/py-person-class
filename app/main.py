class Person:
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list[Person]:

    if not people:
        return []

    [
        Person(name=person_data["name"], age=person_data["age"])
        for person_data in people
    ]

    for person_data in people:
        name = person_data["name"]
        current_instance = Person.people[name]
        partner_name = person_data.get("wife") or person_data.get("husband")
        if partner_name is not None:
            partner_instance = Person.people.get(partner_name)
            if "wife" in person_data:
                current_instance.wife = partner_instance
            elif "husband" in person_data:
                current_instance.husband = partner_instance
    person_instances = [Person.people[data["name"]] for data in people]

    return person_instances
