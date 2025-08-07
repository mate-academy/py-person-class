class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    person_list = [Person(person["name"], person["age"]) for person in people]

    for i, person in enumerate(people):
        if wife_name := person.get("wife"):
            person_list[i].wife = Person.people[wife_name]
        if husband_name := person.get("husband"):
            person_list[i].husband = Person.people[husband_name]

    return person_list
