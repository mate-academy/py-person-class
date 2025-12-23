class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:
    for person in people:
        Person(person["name"], person["age"])
    for person in people:
        if person.get("wife"):
            Person.people[person["name"]].wife = Person.people
            [person["wife"]]
            Person.people[person["wife"]].husband = Person.people
            [person["name"]]
    return list(Person.people.values())
