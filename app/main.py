class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(item["name"], item["age"]) for item in people]
    for item in people:
        person = Person.people[item["name"]]
        if item.get("wife"):
            person.wife = Person.people[item["wife"]]
        if item.get("husband"):
            person.husband = Person.people[item["husband"]]
    return person_list
