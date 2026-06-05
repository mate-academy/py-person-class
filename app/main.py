class Person:

    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:

    result = [Person(p['name'], p['age']) for p in people]

    for persona in people:
        person = Person.people[persona["name"]]

        if persona.get("wife"):
            person.wife = Person.people[persona["wife"]]

        if persona.get("husband"):
            person.husband = Person.people[persona["husband"]]

    return result
