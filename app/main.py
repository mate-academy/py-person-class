class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    list_with_classes = []
    for person in people:
        list_with_classes.append(
            Person(
                person["name"],
                person["age"],
            )
        )

    for data in people:
        current_person = Person.people[data["name"]]
        if "wife" in data and data["wife"] is not None:
            current_person.wife = Person.people[data["wife"]]
        if "husband" in data and data["husband"] is not None:
            current_person.husband = Person.people[data["husband"]]

    return list_with_classes
