class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for person in people:
        person_list.append(Person(person["name"], person["age"]))

    for person, instance in zip(people, person_list):
        if person.get("wife"):
            instance.wife = Person.people[person["wife"]]
        if person.get("husband"):
            instance.husband = Person.people[person["husband"]]

    return person_list
