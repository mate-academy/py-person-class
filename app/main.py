class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list:
    person_list = []
    for human in people:
        person_list.append(Person(human.get("name"), human.get("age")))
    for i, human in enumerate(people):
        if "wife" in human and human.get("wife") is not None:
            person_list[i].wife = Person.people.get(human["wife"])
        if "husband" in human and human.get("husband") is not None:
            person_list[i].husband = Person.people.get(human["husband"])
    return person_list
