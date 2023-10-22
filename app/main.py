class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    humans = [Person(person["name"], person["age"]) for person in people]
    for human in humans:
        for person in people:
            if (
                "wife" in person
                and person["wife"] is not None
                and human.name == person["name"]
            ):
                human.wife = Person.people[person["wife"]]
            elif "husband" in person and person["husband"] is not None:
                human.husband = Person.people[person["husband"]]
    return humans
