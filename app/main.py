class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()

    person_list = [
        Person(person_one["name"], person_one["age"])
        for person_one in people
    ]

    for i, raw in enumerate(people):

        if raw.get("wife") is not None:
            person_list[i].wife = Person.people[raw["wife"]]

        if raw.get("husband") is not None:
            person_list[i].husband = Person.people[raw["husband"]]

    return person_list
