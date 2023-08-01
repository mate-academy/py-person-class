class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    relations = []
    for human in people:
        name = human["name"]
        age = human["age"]
        relations.append(Person(name, age))
    for human in people:
        if human.get("wife"):
            wife = Person.people[human["wife"]]
            Person.people[human["name"]].wife = wife
        if human.get("husband"):
            husband = Person.people[human["husband"]]
            Person.people[human["name"]].husband = husband
    return relations
