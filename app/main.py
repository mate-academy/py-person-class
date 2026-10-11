class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()

    person_list = [
        Person(person["name"], person["age"])
        for person in people
    ]

    for person_data, person in zip(people, person_list):
        for relation in ("wife", "husband"):
            relative_name = person_data.get(relation)

            if relative_name is not None:
                setattr(person, relation, Person.people[relative_name])

    return person_list
