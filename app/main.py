class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result_list = []
    for unit in people:
        result_list.append(Person(unit["name"], unit["age"]))

    for unit in people:
        if unit.get("wife") is not None:
            instance = Person.people[unit["name"]]
            instance.wife = Person.people[unit["wife"]]
        elif unit.get("husband") is not None:
            instance = Person.people[unit["name"]]
            instance.husband = Person.people[unit["husband"]]
    return list(Person.people.values())
