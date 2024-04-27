class Person:
    people = {}

    def __init__(self, name: str, age: int, **married) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self
        for key, value in married.items():
            if value is not None:
                setattr(self, key, value)


def create_person_list(people: list) -> list:
    for person in people:
        Person(
            person["name"], person["age"], **{
                k: v for k, v in person.items() if k in ["wife", "husband"]
            }
        )
    for person in Person.people.values():
        if hasattr(person, "wife") and person.wife:
            person.wife = Person.people.get(person.wife)
        elif hasattr(person, "husband") and person.husband:
            person.husband = Person.people.get(person.husband)
    return list(Person.people.values())
