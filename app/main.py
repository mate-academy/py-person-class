class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = [Person(soul.get("name"), soul.get("age")) for soul in people]
    for soul in people:
        wife = soul.get("wife")
        husband = soul.get("husband")
        if wife:
            Person.people[soul.get("name")].wife = Person.people[wife]
        if husband:
            Person.people[soul.get("name")].husband = Person.people[husband]
    return result
