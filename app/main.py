class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        new_person = Person(person["name"], person["age"])
        if person.get("wife"):
            new_person.wife = person["wife"]
        elif person.get("husband"):
            new_person.husband = person["husband"]
        person_list.append(new_person)

    for person in person_list:
        if hasattr(person, "wife"):
            person.wife = Person.people[person.wife]
        elif hasattr(person, "husband"):
            person.husband = Person.people[person.husband]

    return person_list
