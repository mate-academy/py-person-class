class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list[Person]:
    Person.people.clear()
    result = [
        Person(person.get("name"), person.get("age"))
        for person in people
    ]
    i = 0
    for person in people:
        if person.get("husband") is not None:
            result[i].husband = Person.people.get(person.get("husband"))
        if person.get("wife") is not None:
            result[i].wife = Person.people.get(person.get("wife"))
        i += 1
    return result
