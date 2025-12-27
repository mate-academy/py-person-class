class Person:

    people = {}

    def __init__(
        self,
        name: str,
        age: int,
    ) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}

    person_list = [
        Person(person.get("name"), person.get("age")) for person in people
    ]  # noqa: E501

    for person in people:
        current_person = Person.people.get(person.get("name"))

        for relation in ("wife", "husband"):
            if person.get(relation):
                setattr(
                    current_person,
                    relation,
                    Person.people.get(person.get(relation)),
                )

    return person_list
