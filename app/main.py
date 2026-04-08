class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}

    people_list = [
        Person(person["name"], person["age"])
        for person in people
    ]
    ref = Person.people

    for person in people:
        possible_relations = ["wife", "husband"]

        for relation in possible_relations:
            if person.get(relation):
                partner_name = person[relation]
                ref[person["name"]].__dict__[relation] = ref[partner_name]

    return people_list
