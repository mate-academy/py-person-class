class Person:
    people = {}
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}
    persons = []
    for person in people:
        name = person["name"]
        age = person["age"]
        persons.append(Person(name, age))
    for person in people:
        name = person["name"]
        obj = Person.people[name]
        if "wife" in person and person["wife"]:
            wife_name = person["wife"]
            if wife_name in Person.people:
                obj.wife = Person.people[wife_name]
            else:
                obj.wife = None
        if "husband" in person and person["husband"]:
            husband_name = person["husband"]
            if husband_name in Person.people:
                obj.husband = Person.people[husband_name]
            else:
                obj.husband = None
    return persons
