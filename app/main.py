class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    people_list = [Person(info["name"], info["age"]) for info in people]

    for info in people:
        if info.get("wife"):
            person = Person.people[info["name"]]
            person.wife = Person.people[info["wife"]]
        if info.get("husband"):
            person = Person.people[info["name"]]
            person.husband = Person.people[info["husband"]]

    return people_list
