class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [
        (Person(new_person["name"], new_person["age"]))
        for new_person in people
    ]
    for person in people:
        current_person = Person.people[person["name"]]
        if person.get("wife"):
            current_person.wife = Person.people[person["wife"]]
        elif person.get("husband"):
            current_person.husband = Person.people[person["husband"]]
    return person_list
