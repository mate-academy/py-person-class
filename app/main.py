class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]
    for idx, person in enumerate(people):
        field = next((f for f in ("wife", "husband")
                      if person.get(f) is not None), None)
        if not field:
            continue
        partner_name = person.get(field)
        partner_obj = Person.people.get(partner_name)
        if partner_obj:
            setattr(person_list[idx], field, partner_obj)
    return person_list
