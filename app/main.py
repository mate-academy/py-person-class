class Person:
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    people_list = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        current_person = Person.people[person["name"]]
        for relation in ("wife", "husband"):
            if person.get(relation):
                partner = person[relation]
                setattr(current_person, relation, Person.people[partner])
    return people_list
