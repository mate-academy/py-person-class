class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    list_of_persons = [
        (Person(person["name"], person["age"])) for person in people
    ]

    for name in people:
        if name.get("wife"):
            Person.people[name["name"]].wife = Person.people[name["wife"]]
        if name.get("husband"):
            Person.people[name["name"]].husband = Person.people[
                name["husband"]
            ]
    return list_of_persons
