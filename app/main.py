class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"])
                   for person in people]
    for hum in people:
        if "wife" in hum and hum["wife"]:
            Person.people[hum["name"]].wife = Person.people[hum["wife"]]
        if "husband" in hum and hum["husband"]:
            Person.people[hum["name"]].husband = Person.people[hum["husband"]]
    return person_list
