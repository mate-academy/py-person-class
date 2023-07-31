class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list[Person]:
    instances = [Person(person["name"], person["age"]) for person in people]

    for index, person in enumerate(people):
        if person.get("wife"):
            instances[index].wife = Person.people.get(person.get("wife"))
        elif person.get("husband"):
            instances[index].husband = Person.people.get(person.get("husband"))
    return instances
