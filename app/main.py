class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_to_create: list) -> list:
    person_list = [Person(name=person["name"], age=person["age"])
                   for person in people_to_create]

    for person in people_to_create:
        current_person = Person.people[person["name"]]
        if person.get("wife", None) is not None:
            current_person.wife = Person.people[person["wife"]]
        elif person.get("husband", None) is not None:
            current_person.husband = Person.people[person["husband"]]

    return person_list
