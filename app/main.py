class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people_list: list) -> list:
    person_list = [
        Person(
            person["name"], person["age"]
        ) for person in people_list
    ]

    for index, person in enumerate(people_list):
        if person.get("wife"):
            person_list[index].wife = Person.people[person["wife"]]
        elif person.get("husband"):
            person_list[index].husband = Person.people[person["husband"]]
    return person_list
