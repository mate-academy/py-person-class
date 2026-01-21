class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result = []

    for person in people:
        pers = Person(person["name"], person["age"])
        result.append(pers)

    for person in people:
        current_person = Person.people[person["name"]]
        if person.get("wife"):
            current_person.wife = Person.people[person["wife"]]
        if person.get("husband"):
            current_person.husband = Person.people[person["husband"]]
    return result
