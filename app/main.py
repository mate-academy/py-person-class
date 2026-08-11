class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = [Person(human["name"], human["age"]) for human in people]

    for person, res in zip(people, result):
        for attr, value in person.items():
            if attr in ("name", "age"):
                continue
            if value is not None:
                setattr(res, attr, Person.people[value])

    for i in range(len(people)):
        for attr, value in people[i].items():
            if attr in ("name", "age"):
                continue
            if value is not None:
                setattr(result[i], attr, Person.people[value])

    return result
