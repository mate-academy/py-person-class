class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    person_instances = [
        Person(person_data["name"], person_data["age"])
        for person_data in people
    ]

    for person_data in people:
        if "wife" in person_data:
            partner_name = person_data["wife"]
            if (
                partner_name is not None
                and partner_name in Person.people
            ):
                Person.people[person_data["name"]].wife = (
                    Person.people[partner_name]
                )

        if "husband" in person_data:
            partner_name = person_data["husband"]
            if (
                partner_name is not None
                and partner_name in Person.people
            ):
                Person.people[person_data["name"]].husband = (
                    Person.people[partner_name]
                )

    return person_instances
