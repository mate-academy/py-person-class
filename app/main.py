class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people.update({name: self})


def create_person_list(people: list) -> list:
    persons_list = [Person(one["name"], one["age"]) for one in people]

    for one in people:
        if "wife" in one and one["wife"] is not None:
            Person.people[one["name"]].wife = Person.people[one["wife"]]
            Person.people[one["wife"]].husband = Person.people[one["name"]]

    return persons_list
