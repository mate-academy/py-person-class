class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [
        Person(name=human["name"],
               age=human["age"])
        for human in people]

    for person in people:
        if wife := person.get("wife"):
            current_person = Person.people[person["name"]]
            current_person.wife = Person.people[wife]
        if husband := person.get("husband"):
            current_person = Person.people[person["name"]]
            current_person.husband = Person.people[husband]

    return person_list
