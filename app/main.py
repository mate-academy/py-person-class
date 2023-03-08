class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(persons: list) -> list:
    person_array = []
    for person in persons:
        person_array.append(Person(name=person["name"], age=person["age"]))
    for person in persons:
        human = Person.people[person["name"]]
        if person.get("wife") is not None:
            human.wife = Person.people[person["wife"]]
        elif person.get("husband") is not None:
            human.husband = Person.people[person["husband"]]
    return person_array
