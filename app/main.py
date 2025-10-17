
class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    user_list = [Person(name=user.get("name"), age=user.get("age")) for user in people]
    for user in people:
        if user.get("wife"):
            Person.people[user["name"]].wife = Person.people[user["wife"]]
        if user.get("husband"):
            Person.people[user["name"]].husband = Person.people[user["husband"]]
    return user_list
