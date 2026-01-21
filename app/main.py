class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result = []
    for peoples in people:
        result.append(Person(peoples["name"], peoples["age"]))
    for peoples in people:
        if None in peoples.values():
            continue
        elif "husband" in peoples.keys():
            Person.people[peoples["name"]].husband = (
                Person.people)[peoples["husband"]]
        elif "wife" in peoples.keys():
            Person.people[peoples["name"]].wife = (
                Person.people)[peoples["wife"]]
    return result
