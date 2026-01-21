class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    for person in people:
        name = person["name"]
        age = person["age"]
        Person(name, age)

    for person in people:
        name = person["name"]
        person_instance = Person.people[name]

        if "wife" in person and person["wife"] is not None:
            wife_name = person["wife"]
            person_instance.wife = Person.people[wife_name]

        if "husband" in person and person["husband"] is not None:
            husband_name = person["husband"]
            person_instance.husband = Person.people[husband_name]

    return list(Person.people.values())



