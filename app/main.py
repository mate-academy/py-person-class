class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    final_list = []

    for human in people:

        final_list.append(
            Person(human["name"], human["age"])
        )

    for human in people:

        if "wife" in human and human["wife"] is not None:
            Person.people[human["name"]].wife = \
                Person.people[human["wife"]]

        if "husband" in human and human["husband"] is not None:
            Person.people[human["name"]].husband = \
                Person.people[human["husband"]]
    return final_list
