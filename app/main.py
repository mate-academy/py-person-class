class Person:
    people = {}

    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    update_list = [Person(person["name"], person["age"]) for person in people]
    for person in range(len(people)):
        for data in range(len(people)):

            if "wife" in people[person] and people[person]["wife"] is not None:
                if people[person]["wife"] == people[data]["name"]:
                    update_list[person].wife = \
                        Person.people[people[data]["name"]]

            if "husband" in people[person] \
                    and people[person]["husband"] is not None:

                if people[person]["husband"] == people[data]["name"]:
                    update_list[person].husband = \
                        Person.people[people[data]["name"]]
    return update_list
