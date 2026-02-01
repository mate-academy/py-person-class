class Person:
    people = {}

    def __init__(self, name: str, age: int, **kwargs) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    new_list = [Person(d["name"], d["age"]) for d in people]
    for dictionary in people:
        if dictionary.get("wife"):
            person = Person.people[dictionary["name"]]
            person.wife = Person.people[dictionary["wife"]]
        if dictionary.get("husband"):
            person = Person.people[dictionary["name"]]
            person.husband = Person.people[dictionary["husband"]]
    return new_list
