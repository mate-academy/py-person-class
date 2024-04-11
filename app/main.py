class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_instances = []

    for human in people:
        person_instances.append(Person(human["name"], human["age"]))
    for human in people:
        if human.get("wife"):
            man = Person.people[human["name"]]
            man.wife = Person.people[human["wife"]]
        elif human.get("husband"):
            woman = Person.people[human["name"]]
            woman.husband = Person.people[human["husband"]]
    return person_instances
