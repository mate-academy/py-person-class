class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:

    person_list = [
        Person(name=person["name"], age=person["age"])
        for person in people
    ]

    for person in people:
        for key in ["wife", "husband"]:
            if key in person and person[key] is not None:
                setattr(
                    Person.people[person["name"]],
                    key,
                    Person.people[person[key]]
                )

    return person_list
