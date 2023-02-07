class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]
    for inf in people:
        if inf.get("wife"):
            Person.people[inf["name"]].wife = Person.people[inf["wife"]]
        if inf.get("husband"):
            Person.people[inf["name"]].husband = Person.people[inf["husband"]]
    return person_list
