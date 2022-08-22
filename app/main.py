class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    for body in people:
        Person(body["name"], body["age"])
    for body in people:
        if "wife" in body and body["wife"]:
            Person.people[body["name"]].wife = \
                Person.people[body["wife"]]
        elif "husband" in body and body["husband"]:
            Person.people[body["name"]].husband = \
                Person.people[body["husband"]]
    return [value for value in Person.people.values()]
