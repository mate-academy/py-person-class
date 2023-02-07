class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self
    pass


def create_person_list(people: list) -> list:
    new_list = []

    for human in people:
        new_human = Person(human["name"], human["age"])
        new_list.append(new_human)

    for person in people:
        if person.get("wife"):
            Person.people[person["name"]].wife =\
                Person.people[person["wife"]]
        if person.get("husband"):
            Person.people[person["name"]].husband =\
                Person.people[person["husband"]]
    return new_list
