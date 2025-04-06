class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    friends = [Person(friend["name"], friend["age"]) for friend in people]

    for i in people:
        isinstance_person = Person.people[i["name"]]
        if i.get("wife"):
            isinstance_person.wife = Person.people[i["wife"]]
        if i.get("husband"):
            isinstance_person.husband = Person.people[i["husband"]]
    return friends
