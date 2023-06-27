class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = []

    for person in people:
        result.append(Person(name=person["name"], age=person["age"]))
    for i in range(len(people)):
        if people[i].get("wife"):
            result[i].wife = Person.people[people[i].get("wife")]
        if people[i].get("husband"):
            result[i].husband = Person.people[people[i].get("husband")]

    return result
