class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = list(
        map(
            lambda pers: Person(pers["name"], pers["age"]), people
        )
    )

    for prs in people:
        if "wife" in prs and prs["wife"] is not None:
            Person.people[prs["name"]].wife = Person.people[prs["wife"]]
        if "husband" in prs and prs["husband"] is not None:
            Person.people[prs["name"]].husband = Person.people[prs["husband"]]

    return person_list
