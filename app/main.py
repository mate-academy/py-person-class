class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    for raw_person in people:
        person = Person(raw_person["name"], raw_person["age"])
        partner = list(raw_person)[2]
        if raw_person[partner]:
            setattr(person, partner, raw_person[partner])
            setattr(person, "partner", partner)
    for person in Person.people.values():
        if hasattr(person, "partner"):
            setattr(person, person.partner,
                    Person.people[getattr(person, person.partner)])
            del person.partner
    return list(Person.people.values())
