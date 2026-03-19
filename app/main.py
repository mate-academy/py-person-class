class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}
    peoples = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        if person.get("wife"):
            wife_instance = Person.people[person["name"]]
            wife_instance.wife = Person.people[person["wife"]]

        if person.get("husband"):
            husband_instance = Person.people[person["name"]]
            husband_instance.husband = Person.people[person["husband"]]

    return peoples
