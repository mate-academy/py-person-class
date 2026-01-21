class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    personal_list = [Person(one["name"], one["age"]) for one in people]
    for one in people:
        if "wife" in one and one["wife"] is not None:
            Person.people[one["name"]].wife = Person.people[one["wife"]]
        if "husband" in one and one["husband"] is not None:
            Person.people[one["name"]].husband = Person.people[one["husband"]]
    return personal_list
