class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:
    new_list = [Person(name=p["name"], age=p["age"]) for p in people]

    for person in people:
        my_person = Person.people[person["name"]]

        if person.get("wife"):
            my_person.wife = Person.people[person["wife"]]
        elif person.get("husband"):
            my_person.husband = Person.people[person["husband"]]

    return new_list
