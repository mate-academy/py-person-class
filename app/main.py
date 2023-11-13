class Person:
    # write your code here
    people = {}

    def __init__(self, name: str, age: int, wife: str, husband: str) -> None:
        self.name = name
        self.age = age
        self.wife = wife
        self.husband = husband
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    for person in people:
        Person.name = person["name"]
        Person.age = person["age"]
        Person.wife = person["wife"]









