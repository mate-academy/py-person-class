class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result = []
    for person in people:
        result.append(Person(person["name"], person["age"]))

    for person in people:
        name = person["name"]
        if "wife" in person and person["wife"]:
            Person.people[name].wife = Person.people.get(person["wife"])
        if "husband" in person and person["husband"]:
            Person.people[name].husband = Person.people.get(person["husband"])
    return result
