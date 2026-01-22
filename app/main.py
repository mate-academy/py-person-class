class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for one in people:
        person_list.append(Person(one["name"], one["age"]))

    for human in people:

        if human.get("wife"):
            husband = Person.people[human["name"]]
            husband.wife = Person.people[human["wife"]]
        if human.get("husband"):
            wife = Person.people[human["name"]]
            wife.husband = Person.people[human["husband"]]

    return person_list
