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
    husband_name = Person.people[person["name"]].husband
    for person in people:
        if person.get("wife"):
            Person.people[person["name"]].wife = Person.people[person["wife"]]
        if person.get("husband"):
            husband_name = Person.people[person["husband"]]
    return list_people
