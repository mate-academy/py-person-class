class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = []
    for human in people:
        name = human["name"]
        age = human["age"]
        person = Person(name, age)
        result.append(person)

    for i in range(len(people)):
        for attr, value in people[i].items():
            if attr in ("name", "age"):
                continue
            if value is not None:
                setattr(result[i], attr, Person.people[value])

    return result
