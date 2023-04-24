class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        Person(person["name"], person["age"])
    for human in people:
        if human.get("husband"):
            Person.people[human["name"]].husband = (
                Person.people[human["husband"]])
        if human.get("wife"):
            Person.people[human["name"]].wife = Person.people[human["wife"]]
        person_list.append(Person.people[human["name"]])
    return person_list
