class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self

    def add_wife(self, name_wife: str) -> None:
        self.wife = Person.people[name_wife]

    def add_husband(self, name_husband: str) -> None:
        self.husband = Person.people[name_husband]


def create_person_list(people: list) -> list:
    result = [Person(person["name"], person["age"]) for person in people]
    for i in range(len(people)):
        if people[i].get("wife") is not None:
            Person.people[people[i]["name"]].add_wife(people[i]["wife"])
        if people[i].get("husband") is not None:
            Person.people[people[i]["name"]].add_husband(people[i]["husband"])

    return result
