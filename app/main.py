class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        person_list.append(Person(person["name"], person["age"]))

    for original, obj in zip(people, person_list):
        if original.get("wife") is not None:
            obj.wife = Person.people[original["wife"]]
        if original.get("husband") is not None:
            obj.husband = Person.people[original["husband"]]
    return person_list
