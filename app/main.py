class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[name] = self

def create_person_list(people):
    person_instances = [Person(person["name"], person["age"]) for person in people]

    for i in range(len(person_instances)):
        person = people[i]
        if person.get("wife") is not None:
            person_instances[i].wife = Person.people[person.get("wife")]
        if person.get("husband") is not None:
            person_instances[i].husband = Person.people[person.get("husband")]
    return person_instances
