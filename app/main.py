class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    for person in people:
        Person(person["name"], person["age"])
    for one in people:
        if one.get("wife"):
            Person.people[one["name"]].wife = Person.people[one["wife"]]
        if one.get("husband"):
            Person.people[one["name"]].husband = Person.people[one["husband"]]
    return [Person.people[one["name"]] for one in people]
