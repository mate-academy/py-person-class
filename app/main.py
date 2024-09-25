class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(peopl: list) -> list[Person]:
    person_list = [Person(person["name"], person["age"]) for person in peopl]
    for person in peopl:
        if person.get("husband"):
            Person.people[person.get("name")].husband \
                = Person.people[person.get("husband")]
        if person.get("wife"):
            Person.people[person.get("name")].wife \
                = Person.people[person.get("wife")]
    return person_list
