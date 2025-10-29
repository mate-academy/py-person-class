class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_objects = [
        Person(person.get("name"), person.get("age"))
        for person in people
    ]

    for person in people:
        person_instance = Person.people[person.get("name")]

        if person.get("wife"):
            person_instance.wife = Person.people[person.get("wife")]
        elif person.get("husband"):
            person_instance.husband = Person.people[person.get("husband")]

    return person_objects
