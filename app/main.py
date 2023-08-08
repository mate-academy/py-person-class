class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    person_list = []

    for man in people:
        person = Person(man["name"], man["age"])

        if "wife" in man and man["wife"] is not None:
            for man2 in people:
                if man["wife"] == man2["name"]:
                    wife = Person(man2["name"], man2["age"])
                    person.wife = wife
                    wife.husband = person

        person_list.append(person)

    return person_list
