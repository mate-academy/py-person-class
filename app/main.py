class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    list_of_persons = [
        Person(name=person["name"], age=person["age"])
        for person in people
    ]
    for per in people:
        if per.get("wife"):
            Person.people[per["name"]].wife = Person.people[per["wife"]]
        elif per.get("husband"):
            Person.people[per["name"]].husband = Person.people[per["husband"]]

    return list_of_persons
