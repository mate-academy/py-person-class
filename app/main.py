class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_list):
    person_instances = []

    for person in people_list:
        person_instances.append(Person(person["name"], person["age"]))

    for person in people_list:
        person_instance = Person.people[person["name"]]
        if "wife" in person and person["wife"]:
            person_instance.wife = Person.people[person["wife"]]
        if "husband" in person and person["husband"]:
            person_instance.husband = Person.people[person["husband"]]

    return list(Person.people.values())
