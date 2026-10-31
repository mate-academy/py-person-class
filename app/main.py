class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    people_list = []
    for human in people:
        person = Person(human["name"], human["age"])
        people_list.append(person)

    for human in people:
        if human.get("husband") and human["husband"] is not None:
            (Person.people[human["name"]].
             husband) = Person.people[human["husband"]]
        if human.get("wife") and human["wife"] is not None:
            Person.people[human["name"]].wife = Person.people[human["wife"]]

    return people_list
