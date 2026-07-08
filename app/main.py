class Person:
    people = {}

    def __init__(self, name: str, age: int, **kwargs) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = [Person(**person) for person in people]

    for person in people:
        person_from_class_attr = Person.people.get(person.get("name"))
        if person.get("wife"):
            person_from_class_attr.wife = Person.people.get(person.get("wife"))
        elif person.get("husband"):
            person_from_class_attr.husband = Person.people.get(
                person.get("husband")
            )

    return result
