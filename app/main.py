class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self

    def __repr__(self) -> str:
        return f"Person(name={self.name}, age={self.age})"


def create_person_list(people: list) -> list:
    Person.people.clear()

    _ = [
        Person(person["name"], person["age"])
        for person in people
    ]

    for person in people:
        spouse = Person.people[person["name"]]
        if person.get("wife"):
            spouse.wife = Person.people[person["wife"]]
        if person.get("husband"):
            spouse.husband = Person.people[person["husband"]]

    return list(Person.people.values())
