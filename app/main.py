class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(friend["name"], friend["age"]) for friend in people]
    for friend in people:
        if friend.get("wife"):
            Person.people[friend["name"]].wife = Person.people[friend["wife"]]
        if friend.get("husband"):
            Person.people[friend["name"]].husband = Person.people[friend["husband"]]
    return person_list
