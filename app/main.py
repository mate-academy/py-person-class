class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]
    for per in people:
        if per.get("husband"):
            Person.people[per["name"]].husband = Person.people[per["husband"]]
        if per.get("wife"):
            Person.people[per["name"]].wife = Person.people[per["wife"]]
    return person_list
