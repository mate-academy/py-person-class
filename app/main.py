class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people.update({self.name: self})


def create_person_list(people: list[dict]) -> list:
    people_list = []
    for person in people:
        people_list.append(Person(person["name"], person["age"]))

    for person in people:

        if "wife" in person and person["wife"] is not None:
            Person.people.get(
                person["name"]
            ).wife = Person.people.get(
                person["wife"])

        elif "husband" in person and person["husband"] is not None:
            Person.people.get(
                person["name"]
            ).husband = Person.people.get(
                person["husband"])

    return people_list
