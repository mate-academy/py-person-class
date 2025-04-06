class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    friends = []
    for friend in people:
        friends.append(Person(friend["name"], friend["age"]))

    for i in people:
        isinstance_person = Person.people[i["name"]]
        if "wife" in i and i["wife"]:
            isinstance_person.wife = Person.people[i["wife"]]
        if "husband" in i and i["husband"]:
            isinstance_person.husband = Person.people[i["husband"]]
    return friends
