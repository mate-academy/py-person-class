class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self
    pass


def create_person_list(people: list) -> list[Person]:
    for person in people:
        Person(person["name"], person["age"])
    for person in people:
        current_person = Person.people[person["name"]]
        if person.get("wife") is not None:
            wife = Person.people[person["wife"]]
            current_person.wife = wife
        elif person.get("husband") is not None:
            husband = Person.people[person["husband"]]
            current_person.husband = husband

    return list(Person.people.values())
    pass
