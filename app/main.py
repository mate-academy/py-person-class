class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    final = []
    # By adding person to a list "final",
    # we add Person instances to Person dict attribute "people"
    for person in people:
        final.append(Person(person["name"], person["age"]))

    # Iterating over Person dict attribute "people" and
    # given dict "people" to find respective wife/husband pairs
    for name, obj in Person.people.items():
        for person in people:
            if name == person["name"] and \
                    "wife" in person and \
                    person["wife"] is not None:
                obj.wife = Person.people[person["wife"]]
            elif name == person["name"] and \
                    "husband" in person and \
                    person["husband"] is not None:
                obj.husband = Person.people[person["husband"]]
    return final
