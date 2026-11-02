class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()

    for person in people:
        [Person(name=person["name"], age=person["age"]) for person in people]

    for person in people:
        current_person = Person.people[person["name"]]

        if person.get("wife") is not None:
            current_person.wife = Person.people[person["wife"]]

        elif person.get("husband") is not None:
            current_person.husband = Person.people[person["husband"]]

    return [Person.people[person["name"]] for person in people]
