

class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result = []
    for person in people:
        temp = Person(person["name"], person["age"])
        result.append(temp)

    for person in people:
        temp = Person.people[person["name"]]
        if "wife" in person and person["wife"] is not None:
            temp.wife = Person.people[person["wife"]]

        if "husband" in person and person["husband"] is not None:
            temp.husband = Person.people[person["husband"]]

    return result
