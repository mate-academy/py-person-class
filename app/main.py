class Person:
    people = {}
    def __init__(self, name: str, age: int, **kwargs) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = []
    for person in people:
        result.append(Person(**person))

    for person in people:
        if person.get("wife"):
            Person.people.get(person.get("name")).wife = Person.people.get(person.get("wife"))
        elif person.get("husband"):
            Person.people.get(person.get("name")).husband = Person.people.get(person.get("husband"))

    return result