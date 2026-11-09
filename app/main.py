class Person:
    people: dict = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(data["name"], data["age"]) for data in people]

    for person, data in zip(person_list, people):
        for key in ("wife", "husband"):
            if data.get(key) is not None:
                setattr(person, key, Person.people[data[key]])

    return person_list
