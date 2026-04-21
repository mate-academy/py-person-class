class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(per["name"], per["age"]) for per in people]
    for index, per in enumerate(people):
        if per.get("wife"):
            person_list[index].wife = Person.people[per["wife"]]
        if per.get("husband"):
            person_list[index].husband = Person.people[per["husband"]]
    return person_list
