
class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict[str, str | int | None]]) -> list:
    person_list = []
    for human in people:
        person_list.append(Person(human["name"], human["age"]))
    for human in people:
        if human.get("wife") is not None:
            a = Person.people.get(human["wife"])
            Person.people[human["name"]].wife = a
        if human.get("husband") is not None:
            b = Person.people.get(human["husband"])
            Person.people[human["name"]].husband = b
    return person_list
