class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [
        Person(person.get("name"), person.get("age"))
        for person in people
    ]

    for person in people:
        current_person = Person.people[person["name"]]

        for relation in ("wife", "husband"):
            if person.get(relation) is not None:
                setattr(
                    current_person,
                    relation,
                    Person.people[person.get(relation)]
                )

    return person_list
