class Person:
    people = {}

    def __init__(
        self,
        name: str,
        age: int,
    ) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result_list = []

    for human in people:
        if (
            human.get("husband") is None
            and human.get("wife") is None
        ):
            new_person = Person(human["name"], human["age"])
            result_list.append(new_person)

        else:
            new_person = Person(human["name"], human["age"])
            result_list.append(new_person)

    for human in people:
        person = Person.people[human["name"]]

        if human.get("husband") is not None:
            person.husband = Person.people[human["husband"]]

        elif human.get("wife") is not None:
            person.wife = Person.people[human["wife"]]

    return result_list
