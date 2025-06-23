class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_objects = []
    for person in people:
        name = person["name"]
        age = person["age"]
        new_person = Person(name, age)
        person_objects.append(new_person)
    for person in people:
        current_person_name = person["name"]
        current_person_object = Person.people[current_person_name]
        if "wife" in person and person["wife"] is not None:
            wife_name = person["wife"]
            wife_person_object = Person.people[wife_name]
            current_person_object.wife = wife_person_object
        if "husband" in person and person["husband"] is not None:
            husband_name = person["husband"]
            husband_person_object = Person.people[husband_name]
            current_person_object.husband = husband_person_object
    return person_objects
