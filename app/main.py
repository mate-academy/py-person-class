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
    for index in range(len(people)):
        if people[index].get("wife") is not None:
            result[index].wife = Person.people[people[index].get("wife")]
        if people[index].get("husband") is not None:
            result[index].husband = Person.people[people[index].get("husband")]

    return result
