class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]
    for person in people:
        person_obj = Person.people[person["name"]]
        if bool(person.get("wife")):
            person_obj.wife = Person.people[person["wife"]]
        elif bool(person.get("husband")):
            person_obj.husband = Person.people[person["husband"]]
    return person_list
