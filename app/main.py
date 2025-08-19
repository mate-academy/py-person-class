class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    list_of_person = []
    for person in people:
        list_of_person.append(Person(person["name"], person["age"]))
    for person in people:
        if "wife" in person and person["wife"] is not None:
            current_person = Person.people[person["name"]]
            wife_person = Person.people[person["wife"]]
            current_person.wife = wife_person
        if "husband" in person and person["husband"] is not None:
            current_person = Person.people[person["name"]]
            husband_person = Person.people[person["husband"]]
            current_person.husband = husband_person
    return list_of_person
