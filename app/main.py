class Person:
    people = {}

    def __init__(
            self,
            name: str,
            age: int
    ) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list[Person]:
    Person.people = {}

    [Person(individual["name"], individual["age"]) for individual in people]

    for individual in people:
        person = Person.people[individual["name"]]
        if individual.get("wife"):
            person.wife = Person.people[individual["wife"]]

        if individual.get("husband"):
            person.husband = Person.people[individual["husband"]]

    return list(Person.people.values())
