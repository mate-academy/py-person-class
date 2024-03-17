# Person class 2024
class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    ls_of_people = [
        Person(name=person["name"],
               age=person["age"])
        for person in people
    ]

    for person in people:
        if "wife" in person.keys() and person["wife"] is not None:
            Person.people[person["name"]].wife = Person.people[person["wife"]]
        if "husband" in person.keys() and person["husband"] is not None:
            Person.people[
                person["name"]].husband = Person.people[
                person["husband"]
            ]

    return ls_of_people
