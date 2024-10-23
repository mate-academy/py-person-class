class Person:
    people = {}

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_list) -> list:
    person_instances = []

    for person in people_list:
        person_instance = Person(person["name"], person["age"])
        person_instances.append(person_instance)

    for person in people_list:
        if "wife" in person and person["wife"]:
            Person.people[person["name"]].wife = Person.people[person["wife"]]
        elif "husband" in person and person["husband"]:
            Person.people[person["name"]].husband = Person.people[person["husband"]]

    return person_instances
