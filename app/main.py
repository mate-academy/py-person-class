class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = [
        Person(
            name=person["name"],
            age=person["age"]
        )
        for person in people
    ]

    for person in people:
        per_obj = Person.people[person["name"]]
        if person.get("wife") is not None:
            per_obj.wife = Person.people[person["wife"]]
        if person.get("husband") is not None:
            per_obj.husband = Person.people[person["husband"]]
    return person_list
