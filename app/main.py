class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        person_list.append(Person(person["name"], person["age"]))
        person_name = Person.people[person["name"]]
        if "wife" in person and person["wife"] in Person.people:
            person_name.wife = Person.people[person["wife"]]
            person_name.wife.husband = person_name
        if "husband" in person and person["husband"] in Person.people:
            person_name.husband = Person.people[person["husband"]]
            person_name.husband.wife = person_name
    return person_list
