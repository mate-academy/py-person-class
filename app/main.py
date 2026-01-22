class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        partner_key = list(person.keys())[2]
        if person[partner_key] is not None:
            partner = Person.people[person[partner_key]]
            if partner_key == "wife":
                Person.people[person["name"]].wife = partner
            else:
                Person.people[person["name"]].husband = partner
    return result
