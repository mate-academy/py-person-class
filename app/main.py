class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [
        Person(name=person["name"], age=person["age"]) for person in people
    ]

    for person in people:
        if wife := person.get("wife"):
            wife_instance = Person.people[wife]
            husband_instance = Person.people[person["name"]]
            husband_instance.wife = wife_instance
        if husband := person.get("husband"):
            husband_instance = Person.people[husband]
            wife_instance = Person.people[person["name"]]
            wife_instance.husband = husband_instance
    return person_list
