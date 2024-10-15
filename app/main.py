class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_list):
    persons = []
    for person in people_list:
        new_person = Person(person["name"], person["age"])
        persons.append(new_person)
    for person in people_list:
        person.get("wife") and setattr(Person.people[person["name"]], "wife", Person.people[person["wife"]])
        person.get("husband") and setattr(Person.people[person["name"]], "husband", Person.people[person["husband"]])
    return persons
