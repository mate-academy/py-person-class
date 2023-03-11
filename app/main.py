class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people.update({self.name: self})


def create_person_list(people: list) -> list:
    result = []
    for person in people:
        Person(name=person["name"], age=person["age"])
    for person in people:
        if person.get("husband"):
            Person.people[person["name"]].husband = Person.people[person["husband"]]
        elif person.get("wife"):
            Person.people[person["name"]].wife = Person.people[person["wife"]]
        result.append(Person.people[person["name"]])
    return result
