class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:

    peoples_objects = [Person(human["name"], human["age"]) for human in people]

    for human in people:

        if human.get("wife"):
            wife = Person.people[human["wife"]]
            Person.people[human["name"]].wife = wife

        if human.get("husband"):
            husband = Person.people[human["husband"]]
            Person.people[human["name"]].husband = husband

    return peoples_objects
