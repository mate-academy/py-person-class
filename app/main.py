class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    people_objects = [
        Person(person["name"], person["age"])
        for person in people
    ]
    for person in people:
        if person.get("wife"):
            husband_obj = Person.people[person["name"]]
            husband_obj.wife = Person.people[person["wife"]]
        elif person.get("husband"):
            wife_obj = Person.people[person["name"]]
            wife_obj.husband = Person.people[person["husband"]]
    return people_objects
