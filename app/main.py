class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    address_objects_list = []
    Person.people = {}
    for person in people:
        address_objects_list.append(Person(person["name"], person["age"]))

    for person in people:
        name = person["name"]
        if "wife" in person and person["wife"] is not None:
            name_partner = person["wife"]
            setattr(
                Person.people[name],
                "wife",
                Person.people[name_partner]
            )

        if "husband" in person and person["husband"] is not None:
            name_partner = person["husband"]
            setattr(
                Person.people[name],
                "husband",
                Person.people[name_partner]
            )

    return address_objects_list
