class Person:

    people = {}

    def __init__(self, name: str = None, age: int = None, **kwargs) -> None:
        self.name = name
        self.age = age
        if "wife" in kwargs and kwargs["wife"] is not None:
            self.wife = kwargs["wife"]
        elif "husband" in kwargs and kwargs["husband"] is not None:
            self.husband = kwargs["husband"]
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = [
        Person(**person) for person in people
    ]
    print(person_list)
    for person in person_list:
        if hasattr(person, "wife"):
            person.wife = Person.people.get(person.wife)
        elif hasattr(person, "husband"):
            person.husband = Person.people.get(person.husband)

    return person_list
