class Person:
    people = {}

    def __init__(
            self,
            name: str,
            age: int
    ) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    person_list = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        curr_person = Person.people[person["name"]]
        if person.get("wife"):
            curr_person.wife = Person.people[person["wife"]]
        if person.get("husband"):
            curr_person.husband = Person.people[person["husband"]]

    return person_list
