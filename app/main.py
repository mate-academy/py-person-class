class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__class__.people[self.name] = self


def create_person_list(people: list) -> list:
    for human in people:
        Person(human["name"], human["age"])
    for human in people:
        if human.get("wife", None):
            Person.people[human["name"]].wife = Person.people[human["wife"]]
        elif human.get("husband", None):
            Person.people[human["name"]].husband = Person.people[human["husband"]]
    return [value for value in Person.people.values()]
