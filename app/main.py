class Person:
    people: dict[str, "Person"] = {}

    def __init__(
        self,
        name: str,
        age: int,
    ) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [
        Person(d_person["name"], d_person["age"]) for d_person in people
    ]

    for d_person in people:
        person = Person.people[d_person["name"]]
        if d_person.get("wife"):
            person.wife = Person.people[d_person["wife"]]
        if d_person.get("husband"):
            person.husband = Person.people[d_person["husband"]]

    return person_list
