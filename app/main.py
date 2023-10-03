class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    list_instances = []
    for man in people:
        name = man["name"]
        age = man["age"]
        list_instances.append(Person(name, age))

    for man in people:
        if man.get("wife"):
            Person.people[man["name"]].wife = Person.people[man["wife"]]
        elif man.get("husband"):
            Person.people[man["name"]].husband = Person.people[man["husband"]]
    return list_instances
