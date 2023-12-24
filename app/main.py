class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:

        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:

    result_list = [Person(person["name"], person["age"]) for person in people]

    for person in people:

        if ("wife" in person) and (not person["wife"] is None):

            Person.people[person["name"]].wife = Person.people[person["wife"]]

        if ("husband" in person) and (not person["husband"] is None):

            Person.people[person["name"]].husband = \
                Person.people[person["husband"]]

    return result_list
