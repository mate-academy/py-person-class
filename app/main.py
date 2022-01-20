class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result = []
    for i in range(len(people)):
        Person(people[i]["name"], people[i]["age"])
        result.append(Person.people[people[i]["name"]])
    for human in people:
        if "wife" in human and human["wife"] is not None:
            Person.people[human["name"]].wife = Person.people[human["wife"]]
        if "husband" in human and human["husband"] is not None:
            Person.people[human["name"]].husband = \
                Person.people[human["husband"]]
    return result
