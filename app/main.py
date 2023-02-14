class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    list_of_persons = [(Person(_["name"], _["age"])) for _ in people]

    for _ in people:
        if _.get("wife"):
            Person.people[_["name"]].wife = Person.people[_["wife"]]
        if _.get("husband"):
            Person.people[_["name"]].husband = Person.people[_["husband"]]
    return list_of_persons
