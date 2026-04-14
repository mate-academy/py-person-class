class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result = []
    for person in people:
        person_list = Person(person["name"], person["age"])
        result.append(person_list)
    for person in people:
        obj = Person.people[person["name"]]
        if person.get("wife"):
            obj.wife = Person.people[person["wife"]]
        if person.get("husband"):
            obj.husband = Person.people[person["husband"]]
    return result
