class Person:
    people = {}

    def __init__(self, name, age=0):
        self.name = name
        self.age = age
        Person.people.update({name: self})


def create_person_list(people: list) -> list:
    result = []
    for person in people:
        new_person = Person(person["name"], person["age"])
        add_partner(person, new_person)
        result.append(new_person)
    return result


def add_partner(person, new_person):
    if "wife" in person.keys() and person.get("wife") is not None:
        wife = Person(person.get("wife"))
        new_person.wife = wife
        wife.husband = new_person
    elif "husband" in person.keys() and person.get("husband") is not None:
        husband = Person(person.get("husband"))
        new_person.husband = husband
        husband.wife = new_person
