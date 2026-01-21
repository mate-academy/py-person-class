class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_data):
    persons = []
    for p in people_data:
        person = Person(p["name"], p["age"])
        persons.append(person)

    for p in people_data:
        person = Person.people[p["name"]]
        if "wife" in p and p["wife"]:
            person.wife = Person.people[p["wife"]]
        elif "husband" in p and p["husband"]:
            person.husband = Person.people[p["husband"]]

    return persons
