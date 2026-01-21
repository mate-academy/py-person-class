class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    people_list = [Person(person["name"], person["age"]) for person in people]
    for person in people:
        person_info = Person.people[person["name"]]
        if person.get("wife"):
            person_info.wife = Person.people[person["wife"]]
        if person.get("husband"):
            person_info.husband = Person.people[person["husband"]]
    return people_list
