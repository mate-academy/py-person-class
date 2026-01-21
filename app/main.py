class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for friend in people:
        person = Person(friend["name"], friend["age"])
        person_list.append(person)
    for friend in people:
        if friend.get("wife") is not None:
            Person.people[friend["name"]].wife = Person.people[friend["wife"]]
        if friend.get("husband") is not None:
            Person.people[friend["name"]].husband = \
                Person.people[friend["husband"]]
    return person_list
