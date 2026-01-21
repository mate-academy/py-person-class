class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:

    person_list = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        if person.get("wife") is not None:
            Person.people[person["wife"]].husband = (
                Person.people)[person["name"]]
        elif person.get("husband") is not None:
            Person.people[person["husband"]].wife = (
                Person.people)[person["name"]]
    return person_list
