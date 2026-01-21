class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    list_with_persons = [(Person(one["name"], one["age"])) for one in people]

    for one in people:
        if one.get("wife") is not None:
            Person.people[one["name"]].wife = Person.people[one["wife"]]
        if one.get("husband") is not None:
            Person.people[one["name"]].husband = Person.people[one["husband"]]

    return list_with_persons
