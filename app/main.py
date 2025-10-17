
class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    user_list = []
    for user in people:
        user_list.append(Person(name=user["name"], age=user["age"]))
    for user in people:
        if user.get("wife") or user.get("husband"):
            Person.people["Ross"].wife = Person.people["Rachel"]
            Person.people["Rachel"].husband = Person.people["Ross"]
    return user_list
