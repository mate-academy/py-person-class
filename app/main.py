class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}
    original = people.copy()
    persons = [Person(person["name"], person["age"]) for person in original]

    for person in original:
        if person.get("wife") is not None:
            Person.people[person["name"]].wife = Person.people[person["wife"]]

    for person in original:
        if person.get("husband") is not None:
            Person.people[person["name"]].husband \
                = Person.people[person["husband"]]

    return persons
