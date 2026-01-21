class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        person_list.append(Person(person["name"], person["age"]))
    for person in people:
        if person.get("wife"):
            man = Person.people[person["name"]]
            man.wife = Person.people[person["wife"]]
        if person.get("husband"):
            woman = Person.people[person["name"]]
            woman.husband = Person.people[person["husband"]]
    return person_list
