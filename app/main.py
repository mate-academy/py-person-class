class Person:
    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for person in people:
        person_list.append((Person(person["name"], person["age"])))

    for person in people:
        persons = Person.people[person["name"]]
        if person.get("husband"):
            persons.husband = Person.people[person["husband"]]
        elif person.get("wife"):
            persons.wife = Person.people[person["wife"]]

    return person_list
