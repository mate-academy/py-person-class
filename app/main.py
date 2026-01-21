class Person:
    people = {}

    def __init__(self, name: str, age: int, **kwargs) -> None:
        self.name = name
        self.age = age
        self.kwargs = kwargs
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        person_list.append(Person(**person))

    for person in person_list:
        if person.kwargs.get("wife"):
            person.wife = Person.people[person.kwargs["wife"]]
            person.wife.husband = person
    return person_list
