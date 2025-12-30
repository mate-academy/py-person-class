class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    # Primeira passada: criar instâncias
    for person in people:
        Person(person["name"], person["age"])

    # Segunda passada: criar relacionamentos
    for person in people:
        current_person = Person.people[person["name"]]

        if person.get("wife") is not None:
            current_person.wife = Person.people[person["wife"]]

        if person.get("husband") is not None:
            current_person.husband = Person.people[person["husband"]]

    return list(Person.people.values())
