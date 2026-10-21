class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for data in people:
        person = Person(data["name"], data["age"])
        person_list.append(person)

    for data in people:
        person = Person.people[data["name"]]
        for role in ("wife", "husband"):
            spouse_name = data.get(role)
            if spouse_name is not None:
                setattr(person, role, Person.people[spouse_name])
    return person_list
