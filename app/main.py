class Person:
    people = {}

    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age
        self.people.update({self.name: self})


def create_person_list(people: list) -> list:
    result = [Person(person["name"], person["age"]) for person in people]

    for name_wife in people:
        if name_wife.get("wife") is not None:
            Person.people[
                name_wife["name"]].wife = (
                Person.people
            )[name_wife["wife"]
              ]
            Person.people[
                name_wife["name"]].wife.husband = (
                Person.people
            )[name_wife["name"]
              ]

    return result
