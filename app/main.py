class Person:
    people = {}

    def __init__(
            self, name: str, age: int,
    ) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result = []
    for person in people:
        result.append(
            Person(person["name"], person["age"])
        )

    for number, person in enumerate(people):
        if person.get("wife") is not None:
            result[number].wife = Person.people[person["wife"]]
        elif person.get("husband") is not None:
            result[number].husband = Person.people[person["husband"]]
    return result
