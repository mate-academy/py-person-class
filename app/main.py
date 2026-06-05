class Person:

    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:

    result = []

    for persona in people:
        person = Person(persona["name"],
                        persona["age"]
                        )
        result.append(person)

    for persona in people:
        person = Person.people[persona["name"]]

        if "wife" in persona and persona["wife"] is not None:
            person.wife = Person.people[persona["wife"]]

        if "husband" in persona and persona["husband"] is not None:
            person.husband = Person.people[persona["husband"]]

    return result
