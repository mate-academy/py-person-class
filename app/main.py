class Person:
    people = {}


    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self

def create_person_list(people: list) -> list:
    persons = []
    for person in people:
        new_person = Person(person["name"], person["age"])
        persons.append(new_person)
    for person, new_person in zip(people, persons):
        if person.get("wife"):
            new_person.wife = Person.people[person["wife"]]
        elif person.get("husband"):
            new_person.husband = Person.people[person["husband"]]
    return persons
