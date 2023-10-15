class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people.update({self.name: self})


def create_person_list(people: list) -> list:
    data = []

    for person in people:
        data.append(Person(person["name"], person["age"]))

    for human in people:
        if bool(human.get("wife")):
            Person.people[human["name"]].wife = Person.people[human["wife"]]
        if bool(human.get("husband")):
            Person.people[human["name"]].husband = Person.people[human["husband"]]

    return data
