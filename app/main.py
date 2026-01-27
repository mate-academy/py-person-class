class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    person_list = [
        Person(name=person["name"], age=person["age"])
        for person in people
    ]

    for person_dict in people:
        for partner_key in ["wife", "husband"]:
            partner_name = person_dict.get(partner_key)
            if partner_name is not None:
                current_person = Person.people[person_dict["name"]]
                partner_obj = Person.people[partner_name]
                setattr(current_person, partner_key, partner_obj)

    return person_list
