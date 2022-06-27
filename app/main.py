class Person:

    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    people_list = [Person(human["name"], human["age"]) for human in people]

    for i in people:

        if i.get("wife"):
            Person.people[i["name"]].wife = Person.people[i["wife"]]

        elif i.get("husband"):
            Person.people[i["name"]].husband = Person.people[i["husband"]]

    return people_list