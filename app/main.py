class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    person_list = [Person(peeps["name"], peeps["age"]) for peeps in people]
    for peeps in people:
        inst = Person.people[peeps["name"]]
        wife_name = peeps.get("wife")
        husband_name = peeps.get("husband")
        if wife_name:
            inst.wife = Person.people[wife_name]
        if husband_name:
            inst.husband = Person.people[husband_name]
    return person_list
