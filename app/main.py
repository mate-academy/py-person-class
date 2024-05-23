class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[f"{self.name}"] = self

    def __str__(self) -> str:
        return f"{self.name} {self.age}"


def create_person_list(people: list) -> list:
    out_list = []

    for person in people:
        out_list.append(Person(person["name"], person["age"]))

    for person in people:
        if "wife" in person:
            if person["wife"]:
                Person.people[person["name"]].wife = \
                    Person.people[person["wife"]]

        if "husband" in person:
            if person["husband"]:
                Person.people[person["name"]].husband = \
                    Person.people[person["husband"]]

    return out_list
