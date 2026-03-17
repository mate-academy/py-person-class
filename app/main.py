class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(guys: list[dict]) -> list[Person]:
    result = [Person(guy["name"], guy["age"]) for guy in guys]
    for person in guys:
        if person.get("wife"):
            Person.people[person["name"]].wife = Person.people[person["wife"]]
        elif person.get("husband"):
            Person.people[person["name"]].husband \
                = Person.people[person["husband"]]

    return result
