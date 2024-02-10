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
        Person(given_person["name"], given_person["age"])
        for given_person in people
    ]

    for given_person in people:
        person = Person.people[given_person["name"]]
        if given_person.get("wife"):
            person.wife = Person.people[given_person["wife"]]
        if given_person.get("husband"):
            person.husband = Person.people[given_person["husband"]]

    return person_list
