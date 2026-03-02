class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    list_person = [Person(person["name"], person["age"]) for person in people]
    for person in people:
        current_person = Person.people[person["name"]]
        for relation in ("wife", "husband"):
            if person.get(relation):
                related_person = Person.people.get(person[relation])
                setattr(current_person, relation, related_person)
    return list_person
