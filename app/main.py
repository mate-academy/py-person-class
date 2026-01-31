class Person:
    people = {}
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[name] = self
def create_person_list(people):
    result = []
    for person in people:
        result.append(Person(person["name"], person["age"]))
    for person in people:
        person = Person.people[person["name"]]
        if "wife" in person and person["wife"]:
            person.wife = Person.people[p["wife"]]
        if "husband" in person and person["husband"]:
            person.husband = Person.people[person["husband"]]
    return result
