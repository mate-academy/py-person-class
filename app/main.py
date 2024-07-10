class Person:
    people: dict = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    persons_list = [
        Person(name=user["name"], age=user["age"])
        for user in people
    ]

    for user in people:
        person = Person.people.get(user["name"])
        if user.get("wife"):
            person.wife = Person.people.get(user["wife"])
        if user.get("husband"):
            person.husband = Person.people.get(user["husband"])

    return persons_list
