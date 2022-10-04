class Person:
    people = dict()

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    people_objects = []

    for person in people:
        person_to_add = Person(person["name"], person["age"])
        if person.get("wife"):
            person_to_add.wife = person["wife"]
        if person.get("husband"):
            person_to_add.husband = person["husband"]
        people_objects.append(person_to_add)

    for person in Person.people.values():
        if hasattr(person, "wife") and person.wife:
            person.wife = Person.people[person.wife]
        if hasattr(person, "husband") and person.husband:
            person.husband = Person.people[person.husband]

    return people_objects
