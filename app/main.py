class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[name] = self

def create_person_list(people):
    person_instances = []
    for person_info in people:
        person = Person(person_info["name"], person_info["age"])
        person_instances.append(person)
    return person_instances
