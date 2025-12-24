class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self

    def set_spouse(self, relation: str, partner: "Person") -> None:
        if not hasattr(self, relation):
            setattr(self, relation, partner)
            setattr(partner, "husband" if relation == "wife" else "wife", self)


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        current_person = Person.people[person["name"]]
        for relation in ("wife", "husband"):
            partner_name = person.get(relation)
            if partner_name:
                partner = Person.people[partner_name]
                current_person.set_spouse(relation, partner)

    return person_list
