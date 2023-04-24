class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    list_partners = []
    for human in people:
        list_partners.append(Person(human["name"], human["age"]))
    for human in people:
        if human.get("wife"):
            Person.people[human["name"]].wife = Person.people[human["wife"]]
        elif human.get("husband"):
            Person.people[human["name"]].husband = \
                Person.people[human["husband"]]
    return list_partners
