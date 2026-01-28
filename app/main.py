class Person:
    people = {}

    def __init__(self, name: str, age: int, **kwargs) -> None:
        self.name = name
        self.age = age
        self.__dict__.update({k: v
                              for k, v in kwargs.items() if v is not None})
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_instances = [Person(**person) for person in people]

    for person in person_instances:
        if hasattr(person, "wife"):
            person.wife = Person.people.get(person.wife)
        if hasattr(person, "husband"):
            person.husband = Person.people.get(person.husband)

    return person_instances
