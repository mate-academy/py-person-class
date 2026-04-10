class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    [Person(person["name"], person["age"]) for person in people]

    for person in people:
        if person.get("wife"):
            Person.people[person["name"]].wife \
                = Person.people.get(person["wife"])
        elif person.get("husband"):
            Person.people[person["name"]].husband \
                = Person.people.get(person["husband"])

    return list(Person.people.values())
