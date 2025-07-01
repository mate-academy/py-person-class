class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list[Person]:
    persons = [Person(p_dict["name"], p_dict["age"]) for p_dict in people]

    for person_dict in people:
        person = Person.people[person_dict["name"]]

        partner_husband = person_dict.get("husband", None)
        partner_wife = person_dict.get("wife", None)

        if partner_husband is not None:
            person.husband = Person.people[partner_husband]
        if partner_wife is not None:
            person.wife = Person.people[partner_wife]
    return persons
