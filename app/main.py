class Person:

    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    people_list = [Person(h["name"], h["age"]) for h in people]

    for human in people:
        name_human = Person.people[human["name"]]
        if human.get("wife"):
            name_human.wife = Person.people[human["wife"]]
        elif human.get("husband"):
            name_human.husband = Person.people[human["husband"]]

    return people_list
