class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    for person_data in people:
        Person(name=person_data["name"], age=person_data["age"])

    for person in people:
        if person.get("wife"):
            wife_object = Person.people[person["wife"]]
            wife_object.husband = Person.people[person["name"]]
        if person.get("husband"):
            husband_object = Person.people[person["husband"]]
            husband_object.wife = Person.people[person["name"]]
    return [*Person.people.values()]
