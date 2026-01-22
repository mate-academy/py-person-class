class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    for person_data in people:
        name = person_data["name"]
        age = person_data["age"]
        Person(name, age)

    for person_data in people:
        name = person_data["name"]
        person_instance = Person.people[name]

        for role in ("wife", "husband"):
            if role in person_data and person_data[role] is not None:
                partner_name = person_data[role]
                partner_instance = Person.people[partner_name]
                setattr(person_instance, role, partner_instance)

    return list(Person.people.values())
