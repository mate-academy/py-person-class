class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    [Person(person["name"], person["age"]) for person in people]

    for person_dict in people:
        if "wife" in person_dict and person_dict["wife"] is not None:
            Person.people[person_dict["name"]].wife = (
                Person.people)[person_dict["wife"]]
            Person.people[person_dict["wife"]].husband = (
                Person.people)[person_dict["name"]]

    return [*Person.people.values()]
