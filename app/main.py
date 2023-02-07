class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    instances_ls = [Person(person["name"], person["age"]) for person in people]
    for person in people:
        pair = person.get("wife") or person.get("husband")
        name = person["name"]
        if pair and "wife" in person:
            Person.people[name].wife = Person.people[pair]
        elif pair and "husband" in person:
            Person.people[name].husband = Person.people[pair]
    return instances_ls
