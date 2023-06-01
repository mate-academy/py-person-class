class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    ls = [Person(name=person["name"], age=person["age"]) for person in people]
    for person in people:
        new_person = Person.people[person["name"]]
        if person.get("wife"):
            new_person.wife = (Person.people[person["wife"]])
        elif person.get("husband"):
            new_person.husband = (Person.people[person["husband"]])
    return ls
