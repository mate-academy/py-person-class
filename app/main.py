class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        person_list.append(Person(person["name"], person["age"]))
    for per in people:
        if per.get("wife"):
            Person.people[per["name"]].wife = Person.people[per["wife"]]
        elif per.get("husband"):
            Person.people[per["name"]].husband = Person.people[per["husband"]]

    return person_list
