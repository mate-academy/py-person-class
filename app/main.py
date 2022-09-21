class Person:
    people = {}

    def __init__(self,
                 name,
                 age):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    list_people = [Person(person["name"], person["age"]) for person in people]
    for person in people:
        person_name = Person.people[person["name"]]
        if person.get("wife"):
            person_name.wife = Person.people[person["wife"]]
        if person.get("husband"):
             person_name.husband = Person.people[person["husband"]]
    return list_people
