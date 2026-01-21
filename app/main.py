class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.name = name
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = [Person(human["name"], human["age"]) for human in people]
    name_person = {person.name: person for person in result}
    for i, human in enumerate(people):
        if "wife" in human and human["wife"] is not None:
            result[i].wife = name_person.get(human["wife"])
        if "husband" in human and human["husband"] is not None:
            result[i].husband = name_person.get(human["husband"])
    return result
