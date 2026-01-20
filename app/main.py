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

        if person.get("wife") is not None:
            wife = Person.people.get(person["wife"])
            person_object.wife = wife
        if person.get("husband") is not None:
            husband = Person.people.get(person["husband"])
            person_object.husband = husband

    return person_objects
