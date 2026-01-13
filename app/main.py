class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]
    for i, person in enumerate(people):
        for relation in ("wife", "husband"):
            if person.get(relation):
                setattr(
                    person_list[i],
                    relation,
                    Person.people[person[relation]]
                )
    return person_list
