class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        goal_person = Person.people[person["name"]]

        if "wife" in person and person["wife"] is not None:
            goal_person.wife = Person.people[person["wife"]]

        if "husband" in person and person["husband"] is not None:
            goal_person.husband = Person.people[person["husband"]]

    return person_list
