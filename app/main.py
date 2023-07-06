class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    for person in people:
        Person(person["name"], person["age"])
    for person in people:
        if person.get("wife") is not None:
            wife = Person.people[person["wife"]]
            Person.people[person["name"]].wife = wife
        if person.get("husband") is not None:
            husband = Person.people[person["husband"]]
            Person.people[person["name"]].husband = husband
    return [person for person in Person.people.values()]
