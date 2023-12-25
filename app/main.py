class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people.update({name: self})


def create_person_list(people: list) -> list:
    return [
        Person(person["name"],
               person["age"])
               # person["wife"] if "wife" in person else person["husband"],
               # person["spouse_name"])
        for person in people
    ]
