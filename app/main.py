class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self
    pass


def create_person_list(people: list) -> list:
    Person.people.clear()

    for person in people:
        Person(person["name"], person["age"])

    return [
        add_spouse(person) for person in people
    ]


def add_spouse(person: object) -> object:
    person_obj = Person.people[person["name"]]
    if person.get("wife"):
        person_obj.wife = Person.people[person["wife"]]
    elif person.get("husband"):
        person_obj.husband = Person.people[person["husband"]]
    return person_obj
