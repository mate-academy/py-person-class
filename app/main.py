class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result = []
    for person in people:
        current = Person(person["name"], person["age"])
        result.append(current)

    for person in people:
        if person.get("husband") is not None:
            Person.people[person["name"]].husband = (
                Person.people)[person["husband"]]
            Person.people[person["husband"]].wife = (
                Person.people)[person["name"]]
        if person.get("wife") is not None:
            Person.people[person["name"]].wife = (
                Person.people)[person["wife"]]
            Person.people[person["wife"]].husband = (
                Person.people)[person["name"]]
    return result
