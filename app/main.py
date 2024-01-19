class Person:
    people = {}
    def __init__(self, name, age):
        self.name = name
        self.age = age

        Person.people[name] = self

def create_person_list(people: list) -> list:
    persons =[]
    for person in people:
        Person(person["name"], person["age"])

    for person in people:
        person_obj = Person.people[person["name"]]
        # Add spouse only if the key exists
        if "wife" in person and person["wife"]:
            person_obj.wife = Person.people[person["wife"]]
        if "husband" in person and person["husband"]:
            person_obj.husband = Person.people[person["husband"]]

    # Build the list of Person instances without using a list comprehension
    person_list = []
    for person in people:
        person_list.append(Person.people[person["name"]])

    return person_list
