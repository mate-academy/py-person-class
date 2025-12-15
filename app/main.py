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

    for individual in people:
        Person(individual["name"], individual["age"])

    for individual in people:
        person = Person.people[individual["name"]]
        if "wife" in individual:
            if individual["wife"]:
                person.wife = Person.people[individual["wife"]]

        if "husband" in individual:
            if individual["husband"]:
                person.husband = Person.people[individual["husband"]]

    return list(Person.people.values())
