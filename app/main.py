class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list[Person]:
    for dictionary in people:
        Person(dictionary["name"], dictionary["age"])

    for dictionary in people:
        if "wife" in dictionary:
            if dictionary["wife"] is None:
                continue
            else:
                Person.people[dictionary["name"]].wife = (
                    Person.people)[dictionary["wife"]]
        else:
            if dictionary["husband"] is None:
                continue
            else:
                Person.people[dictionary["name"]].husband = (
                    Person.people)[dictionary["husband"]]
    return [value for value in Person.people.values()]
