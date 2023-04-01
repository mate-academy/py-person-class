class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    result = [
        Person(person.get("name"), person.get("age")) for person in people
    ]

    for i in range(len(people)):
        if people[i].get("wife") is not None:
            result[i].wife = Person.people.get(people[i]["wife"])
        if people[i].get("husband") is not None:
            result[i].husband = Person.people.get(people[i]["husband"])

    return result
