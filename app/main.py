
class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}

    person_list = [
        Person(person["name"], person["age"])
        for person in people
    ]

    for person, person_obj in zip(people, person_list):
        if person.get("wife") is not None:
            person_obj.wife = Person.people[person["wife"]]

        if person.get("husband") is not None:
            person_obj.husband = Person.people[person["husband"]]

    return person_list
