class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    Person.people = {}

    [Person(person["name"], person["age"]) for person in people]

    for person in people:
        current_instance = Person.people[person["name"]]

        if person.get("husband"):
            current_instance.husband = Person.people[person["husband"]]

        elif person.get("wife"):
            current_instance.wife = Person.people[person["wife"]]

    return list(Person.people.values())
