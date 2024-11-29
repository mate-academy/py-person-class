class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self

    @staticmethod
    def link_people() -> None:
        for person in Person.people.values():
            if hasattr(person, "husband") and isinstance(person.husband, str):
                partner_name = person.husband
                person.husband = Person.people.get(partner_name)
            if hasattr(person, "wife") and isinstance(person.wife, str):
                partner_name = person.wife
                person.wife = Person.people.get(partner_name)


def create_person_list(people: list[dict]) -> list[Person]:
    for person_dict in people:
        name = person_dict["name"]
        age = person_dict["age"]
        person = Person(name, age)
        if "husband" in person_dict and person_dict["husband"] is not None:
            person.husband = person_dict["husband"]
        if "wife" in person_dict and person_dict["wife"] is not None:
            person.wife = person_dict["wife"]

    Person.link_people()

    return list(Person.people.values())
