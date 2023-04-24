class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    friends = []
    for human in people:
        friend = Person(human["name"], human["age"])
        friends.append(friend)
    for pos, human in enumerate(people):
        if "wife" in human and human["wife"] is not None:
            friends[pos].wife = Person.people[human["wife"]]
        if "husband" in human and human["husband"] is not None:
            friends[pos].husband = Person.people[human["husband"]]
    return friends
