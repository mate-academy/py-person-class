class Person:
    people: dict = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    result_list: list = []

    for person in people:
        result_list.append(Person(name=person["name"], age=person["age"]))

    for person in people:
        if "wife" in person.keys() and person["wife"] is not None:
            if person["wife"] in Person.people.keys():
                Person.people[person["name"]].wife = (
                    Person.people)[person["wife"]]
        elif "husband" in person.keys() and person["husband"] is not None:
            if person["husband"] in Person.people.keys():
                Person.people[person["name"]].husband = (
                    Person.people)[person["husband"]]

    return result_list
