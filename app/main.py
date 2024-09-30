class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    person_instances = []
    name_to_instance = {}

    for person_data in people:
        person = Person(person_data["name"], person_data["age"])
        person_instances.append(person)
        name_to_instance[person.name] = person

    for person_data in people:
        if "wife" in person_data:
            partner_name = person_data["wife"]
            if partner_name is not None and partner_name in name_to_instance:
                name_to_instance[person_data["name"]].wife = (
                    name_to_instance[partner_name]
                )

        if "husband" in person_data:
            partner_name = person_data["husband"]
            if partner_name is not None and partner_name in name_to_instance:
                name_to_instance[person_data["name"]].husband = (
                    name_to_instance[partner_name]
                )

    for person in person_instances:
        if person.wife is None:
            del person.wife

        if person.husband is None:
            del person.husband

    return person_instances
