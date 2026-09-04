class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[name] = self


def create_person_list(people: list) -> list:

    new_list = [Person(friend["name"], friend["age"]) for friend in people]

    for friend in people:
        if friend.get("wife"):
            Person.people[friend["name"]].wife = (
                Person.people[friend.get("wife")]
            )

    for friend in people:
        if friend.get("husband"):
            Person.people[friend["name"]].husband = (
                Person.people[friend.get("husband")]
            )

    return new_list
