class Person:

    people = {}

    def __init__(self, name: str, age: int) -> any:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:

    for person in people:
        name = person["name"]
        age = person["age"]
        Person(name, age)

    for person in people:
        name = person["name"]
        current_person = Person.people[name]
        if "wife" in person and person["wife"]:
            current_person.wife = Person.people[person["wife"]]
            current_person.wife.husband = current_person
        if "husband" in person and person["husband"]:
            current_person.husband = Person.people[person["husband"]]
            current_person.husband.wife = current_person

    return list(Person.people.values())
