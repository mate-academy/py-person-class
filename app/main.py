class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    people_list = [
        Person(person["name"], person["age"]) for person in people
    ]
    for person in people:
        print(person.get("wife"))
        print(person.get("husband"))
        if person.get("wife"):
            Person.people[person["name"]].wife = Person.people[person["wife"]]
        elif person.get("husband"):
            husband = Person.people[person["husband"]]
            Person.people[person["name"]].husband = husband

    return people_list
