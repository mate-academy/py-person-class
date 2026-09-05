class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for person_dict in people:
        person = Person(person_dict["name"], person_dict["age"])
        person_list.append(person)

    for person_dict, person in zip(people, person_list):
        for key in ("wife", "husband"):
            if key in person_dict and person_dict[key] is not None:
                partner_name = person_dict[key]
                partner = Person.people[partner_name]
                setattr(person, key, partner)

    return person_list
