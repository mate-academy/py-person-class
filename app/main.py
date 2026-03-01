class Person:

    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[self.name] = self


def create_person_list(people: list[dict]) -> list[Person]:

    Person.people.clear()
    person_instances = [Person(person.get("name"), person.get("age"))
                        for person in people]

    for person_data in people:
        current_name = person_data.get("name")
        current_person = Person.people.get(current_name)

        is_wife = "wife" in person_data
        partner_key = "wife" if is_wife else "husband"
        partner_name = person_data.get(partner_key)

        if partner_name is not None:
            partner_instance = Person.people.get(partner_name)
            setattr(current_person, partner_key, partner_instance)

    return person_instances
