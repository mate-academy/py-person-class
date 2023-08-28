class Person:
    people = {}

    def __init__(
            self,
            name: str,
            age: int
    ) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    result: list = []

    for man in people:
        new_person: Person = Person(
            man["name"],
            man["age"]
        )
        if man.get("wife"):
            new_person.wife = Person.people[man["name"]]
            Person.people[man["name"]].husband = new_person
        if man.get("husband"):
            new_person.husband = Person.people[man["name"]]
            Person.people[man["name"]].wife = new_person

        result.append(new_person)

    return result
