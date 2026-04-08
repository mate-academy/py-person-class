class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


def create_person_list(people: list) -> list:
    reference = Person.people

    for person in people:
        reference[person["name"]] = Person(person["name"], person["age"])

    for person in people:
        possible_relations = ["wife", "husband"]

        for relation in possible_relations:
            if person.get(relation):
                partner_name = person[relation]
                reference[person["name"]].__dict__[relation] = reference[partner_name]

    return [person for person in reference.values()]
