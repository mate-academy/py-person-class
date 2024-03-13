class Person:
    people: dict = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    result_list: list = [
        Person(name=person["name"], age=person["age"]) for person in people
    ]

    for person in people:
        if person.get("wife") and person["wife"] in Person.people:
            Person.people[person["name"]].wife = (
                Person.people)[person["wife"]]
        elif person.get("husband") and person["husband"] in Person.people:
            Person.people[person["name"]].husband = (
                Person.people)[person["husband"]]

    return result_list
