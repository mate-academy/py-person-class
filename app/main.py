class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]
    for person in people:
        if not person.get("wife") is None:
            Person.people[person["name"]].wife = Person.people[person["wife"]]
        if not person.get("husband") is None:
            Person.people[person["name"]].husband = (
                Person.people)[person["husband"]]
    return person_list
