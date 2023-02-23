class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    people_list = []
    for person in people:
        people_list.append(Person(person["name"], person["age"]))
    for person in people:
        if person.get("wife"):
            Person.people[person["name"]].wife = Person.people[person["wife"]]
        if person.get("husband"):
            husband = Person.people[person["husband"]]
            Person.people[person["name"]].husband = husband
    return people_list
