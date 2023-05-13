class Person:
    people = {}

    def __init__(
            self,
            name: str,
            age: int,
    ) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    person_list = [
        Person(
            person.get("name"),
            person.get("age")
        )
        for person in people
    ]
    for num, person in enumerate(people):
        if person.get("wife"):
            person_list[num].wife = Person.people.get(person["wife"])
        elif person.get("husband"):
            person_list[num].husband = Person.people.get(person["husband"])
    return person_list
