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

    for person in people:
        partner_key = "wife" if "wife" in person else "husband"
        partner_name = person.get(partner_key)
        if partner_name:
            person_instance = person_instances[person["name"]]
            partner_instance = person_instances[partner_name]
            setattr(person_instance, partner_key, partner_instance)

    return list(person_instances.values())
