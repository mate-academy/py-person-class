class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    obj_people = [Person(man["name"], man["age"]) for man in people]

    for i, man in enumerate(people):
        if man.get("wife"):
            obj_people[i].wife = Person.people[man["wife"]]
        elif man.get("husband"):
            obj_people[i].husband = Person.people[man["husband"]]

    return obj_people
