class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self
    pass


def create_person_list(people: list) -> list[Person]:
    Person.people = {}
    for person in people:
        Person(person["name"], person["age"])
    for person in people:
        current_person = Person.people[person["name"]]
        if person.get("wife") is not None:
            current_person.wife = Person.people[person["wife"]]
        elif person.get("husband") is not None:
            current_person.husband = Person.people[person["husband"]]

    return list(Person.people.values())

    pass
