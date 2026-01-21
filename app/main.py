class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()

    for person in people:
        Person(person["name"], person["age"])

    for person in people:
        person_ = Person.people[person["name"]]
        if person.get("wife"):
            person_.wife = Person.people[person["wife"]]
        if person.get("husband"):
            person_.husband = Person.people[person["husband"]]

    return [Person.people[data["name"]] for data in people]
