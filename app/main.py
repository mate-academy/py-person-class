class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        if person.get("husband"):
            Person.people[person["name"]].husband = (
                Person.people[person["husband"]]
            )
        elif person.get("wife"):
            Person.people[person["name"]].wife = Person.people[person["wife"]]
    return person_list
