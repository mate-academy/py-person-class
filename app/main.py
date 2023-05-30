class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        name = person["name"]
        age = person["age"]
        person_list.append(Person(name, age))

    for person in people:
        somebody = Person.people[person["name"]]
        if person.get("wife"):
            somebody.wife = Person.people[person["wife"]]
        if person.get("husband"):
            somebody.husband = Person.people[person["husband"]]

    return person_list
