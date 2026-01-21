class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    people_list = [Person(person["name"], person["age"]) for person in people]
    for person in people:
        person_instance = Person.people[person["name"]]
        if person.get("wife"):
            wife_instance = Person.people[person["wife"]]
            person_instance.wife = wife_instance
        if person.get("husband"):
            husband_instance = Person.people[person["husband"]]
            person_instance.husband = husband_instance
    return people_list
