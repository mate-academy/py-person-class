class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people_list: list) -> list:
    Person.people.clear()
    person_list = [
        Person(person["name"], person["age"]) for person in people_list
    ]

    for pos, person in enumerate(person_list):
        if people_list[pos].get("wife"):
            person.wife = Person.people[people_list[pos]["wife"]]
            person.wife.husband = person
        if people_list[pos].get("husband"):
            person.husband = Person.people[people_list[pos]["husband"]]
            person.husband.wife = person

    return person_list
