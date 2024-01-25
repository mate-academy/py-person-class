class Person:
    people = {}

    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self

    def __repr__(self) -> str:
        return f"Person(name={self.name}, age={self.age})"


def create_person_list(people: list) -> list:

    persons = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        if person.get("wife"):
            Person.people[person["name"]].wife = \
                Person.people[person["wife"]]
        elif person.get("husband"):
            Person.people[person["name"]].husband = \
                Person.people[person["husband"]]

    return persons
