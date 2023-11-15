class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [
        Person(person["name"], person["age"])
        for person in people
    ]
    persons = Person.people

    for person in people:
        if wife_name := person.get("wife"):
            persons[person["name"]].wife = persons[wife_name]
        if husband_name := person.get("husband"):
            persons[person["name"]].husband = persons[husband_name]
    return person_list
