class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list:
    for person in people:
        name = person["name"]
        age = person["age"]
        person_instance = Person(name, age)
        Person.people[name] = person_instance

    for person in people:
        name = person["name"]
        if person.get("wife") is not None:
            Person.people[name].wife = Person.people[person["wife"]]
        if person.get("husband") is not None:
            Person.people[name].husband = Person.people[person["husband"]]

    return list(Person.people.values())
