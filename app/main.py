class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list[dict]) -> list:
    list_of_person = [
        Person(person["name"], person["age"])
        for person in people
    ]

    for person in people:
        name_person = Person.people[person["name"]]
        if person.get("husband"):
            name_person.husband = Person.people[person["husband"]]
        elif person.get("wife"):
            name_person.wife = Person.people[person["wife"]]
    return list_of_person
