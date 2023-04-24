class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = [
        Person(person["name"], person["age"])
        for person in people
    ]

    for person in people:
        if person.get("wife") is not None:
            wife = Person.people[person["name"]]
            wife.wife = Person.people[person["wife"]]
        if person.get("husband") is not None:
            husband = Person.people[person["name"]]
            husband.husband = Person.people[person["husband"]]

    return result
