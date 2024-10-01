class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict[str, any]]) -> list[Person]:
    # The following annotations may have issues.
    # Please note that they should be written in capitalized words,
    # and the typing module is imported. ;)
    if not people:
        raise ValueError("The people list is empty")

    person_list = [
        Person(person.get("name"), person.get("age"))
        for person in people
    ]

    for person_data, person_instance in zip(people, person_list):
        if wife := person_data.get("wife"):
            person_instance.wife = Person.people.get(wife)
        elif husband := person_data.get("husband"):
            person_instance.husband = Person.people.get(husband)

    return person_list
