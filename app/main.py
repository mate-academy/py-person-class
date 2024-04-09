class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        person_instance = Person.people[person["name"]]
        if wife_name := person.get("wife"):
            person_instance.wife = Person.people[wife_name]
        elif husband_name := person.get("husband"):
            person_instance.husband = Person.people[husband_name]

    return person_list
