class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_instances = []

    for person_dict in people:
        person = Person(
            name=person_dict["name"],
            age=person_dict["age"],
        )
        person_instances.append(person)

    for person_dict in people:
        person = Person.people[person_dict["name"]]

        if person_dict.get("wife") is not None:
            person.wife = Person.people[person_dict["wife"]]

        if person_dict.get("husband") is not None:
            person.husband = Person.people[person_dict["husband"]]

    for person_dict in people:
        person = Person.people[person_dict["name"]]

    return person_instances
