class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_objects = []

    for person in people:
        person_objects.append(Person(person["name"], person["age"]))

    for person in people:
        current_person = Person.people[person["name"]]

        if "wife" in person and person["wife"]:
            wife_person = Person.people.get(person["wife"])
            if wife_person:
                current_person.wife = wife_person
                wife_person.husband = current_person

        if "husband" in person and person["husband"]:
            husband_person = Person.people.get(person["husband"])
            if husband_person:
                current_person.husband = husband_person
                husband_person.wife = current_person

    for person in person_objects:
        if person.wife is None:
            del person.wife
        if person.husband is None:
            del person.husband
    return person_objects
