class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:

    persons_list = [Person(person["name"], person["age"]) for person in people]

    for person in people:

        if person.get("wife") is not None:

            Person.people[person.get("name")].wife \
                = Person.people[person.get("wife")]

        elif person.get("husband") is not None:

            Person.people[person.get("name")].husband \
                = Person.people[person.get("husband")]

    return persons_list
