class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = [
        Person(name=person["name"], age=person["age"]) for person in people
    ]
    for person in people:
        if "wife" in person and person.get("wife") is not None:
            Person.people.get(person["name"]).wife = (
                Person.people.get(person["wife"])
            )
        elif "husband" in person and person.get("husband") is not None:
            Person.people.get(person["name"]).husband = (
                Person.people.get(person["husband"])
            )
    return person_list
