class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}

    person_list = []

    for person in people:
        new_person = Person(
            person["name"],
            person["age"]
        )
        person_list.append(new_person)

    for person, person_data in zip(person_list, people):
        for relation in ("wife", "husband"):
            if person_data.get(relation) is not None:
                setattr(
                    person,
                    relation,
                    Person.people[person_data[relation]]
                )

    return person_list

