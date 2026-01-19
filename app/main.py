class Person:
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age

        Person.people[self.name] = self


def create_person_list(people: list[dict]) -> list:
    persons = [Person(human["name"], human["age"]) for human in people]

    for human in people:
        if human.get("wife"):
            Person.people[human["name"]].wife = Person.people[human["wife"]]
        elif human.get("husband"):
            Person.people[human["name"]].husband = Person.people[
                human["husband"]]

    return persons
