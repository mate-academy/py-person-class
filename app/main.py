class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    list_of_persons = [
        Person(person["name"], person["age"])
        for person in people
    ]
    for person in people:
        data = Person.people[person["name"]]
        if person.get("wife"):
            data.wife = Person.people.get(person["wife"])
        if person.get("husband"):
            data.husband = Person.people.get(person["husband"])
    return list_of_persons
