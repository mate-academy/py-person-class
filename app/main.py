class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(hum.get("name"), hum.get("age")) for hum in people]
    for i, human in enumerate(people):
        if human.get("wife"):
            person_list[i].wife = Person.people.get(human["wife"])
        if human.get("husband"):
            person_list[i].husband = Person.people.get(human["husband"])
    return person_list
