class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    persons_list = [
        Person(individual["name"], individual["age"])
        for individual in people
    ]

    for person in people:
        name = person["name"]
        if "wife" in person and person["wife"]:
            wife_name = person["wife"]
            actual_person = Person.people[name]
            wife_person = Person.people[wife_name]
            actual_person.wife = wife_person
        elif "husband" in person and person["husband"]:
            husband_name = person["husband"]
            actual_person = Person.people[name]
            husband_person = Person.people[husband_name]
            actual_person.husband = husband_person

    return persons_list
