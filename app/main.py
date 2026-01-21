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
        person_object = Person.people[person.get("name")]
        if person.get("wife"):
            wife = Person.people[person.get("wife")]
            person_object.wife = wife
        elif person.get("husband"):
            husband = Person.people[person.get("husband")]
            person_object.husband = husband
    return person_objects
