class Person:
    people = {}

    def __init__(self, name: str, age: int, **kwargs) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]
    for person in people:
        current_person = Person.people[person["name"]]
        if person.get("wife"):
            wife = Person.people[person["wife"]]
            current_person.wife = wife
        if person.get("husband"):
            husband = Person.people[person["husband"]]
            current_person.husband = husband
    return person_list
