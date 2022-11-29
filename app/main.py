class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    final = []
    # By adding person to a list "final",
    # we add Person instances to Person dict attribute "people"
    for person in people:
        final.append(Person(person["name"], person["age"]))

    # Iterating over Person dict attribute "people" and
    # given dict "people" to find respective wife/husband pairs
    for person in people:
        if person.get("wife") is not None:
            Person.people[person["name"]].wife = \
                Person.people[person["wife"]]
        elif person.get("husband") is not None:
            Person.people[person["name"]].husband = \
                Person.people[person["husband"]]
    return final
