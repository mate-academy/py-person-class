class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for person in people:
        new_person = Person(person["name"], person["age"])
        person_list.append(new_person)

    for person in people:
        current_person = Person.people[person["name"]]

        for relation in ("wife", "husband"):
            if person.get(relation) is not None:
                setattr(
                    current_person,
                    relation,
                    Person.people[person[relation]]
                )

    return person_list
