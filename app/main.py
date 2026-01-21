class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_objects = [
        Person(person["name"], person["age"])
        for person in people
    ]
    for person in people:
        person_object = Person.people[person["name"]]
        if "wife" in person:
            if person["wife"]:
                wife = Person.people[person["wife"]]
                person_object.wife = wife
        elif "husband" in person:
            if person["husband"]:
                husband = Person.people[person["husband"]]
                person_object.husband = husband
    return person_objects
