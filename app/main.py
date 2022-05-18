class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    friends = []
    for hu_man in people:
        friend = Person(hu_man["name"], hu_man["age"])
        friends.append(friend)
    for pos, hu_man in enumerate(people):
        if "wife" in hu_man and hu_man["wife"] is not None:
            friends[pos].wife = Person.people[hu_man["wife"]]
        if "husband" in hu_man and hu_man["husband"] is not None:
            friends[pos].husband = Person.people[hu_man["husband"]]
    return friends
