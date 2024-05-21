class Person:
    people = {}

    def __init__(self, name: str, age: int) -> str | int:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]
    for person in people:
        if person.get("wife"):
            male_man = Person.people[person["name"]]
            male_man.wife = Person.people[person["wife"]]
        elif person.get("husband"):
            male_woman = Person.people[person["name"]]
            male_woman.husband = Person.people[person["husband"]]
    return person_list
