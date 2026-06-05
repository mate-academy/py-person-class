class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    people_list = []
    for person in people:
        new_person = Person(person["name"], person["age"])
        people_list.append(new_person)
    for person in people:
        current = Person.people[person["name"]]
        if person.get("wife"):
            current.wife = Person.people[person["wife"]]
        elif person.get("husband"):
            current.husband = Person.people[person["husband"]]
    return people_list
