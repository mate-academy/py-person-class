class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = [
        Person(name=person["name"], age=person["age"])
        for person in people
    ]

    for person in people:
        if wife := person.get("wife", None):
            male = Person.people.get(person["name"])
            male.wife = Person.people.get(wife)
        elif husband := person.get("husband", None):
            female = Person.people.get(person["name"])
            female.husband = Person.people.get(husband)

    return person_list
