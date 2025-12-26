class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    result = [Person(person["name"], person["age"]) for person in people]
    for index, user in enumerate(people):
        if user.get("wife"):
            result[index].wife = Person.people[user["wife"]]
        if user.get("husband"):
            result[index].husband = Person.people[user["husband"]]
    return result
