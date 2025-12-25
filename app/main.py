class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result = [Person(person["name"], person["age"]) for person in people]
    for person in people:
        for key in ("wife", "husband"):
            if person.get(key) is not None:
                setattr(Person.people[person["name"]],
                        key, Person.people[person[key]])
    return result
