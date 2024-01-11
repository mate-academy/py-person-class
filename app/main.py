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
        temp = Person.people[person["name"]]
        if "wife" in person and person["wife"] in Person.people:
            temp.wife = Person.people[person["wife"]]
            temp.wife.husband = temp
        if "husband" in person and person["husband"] in Person.people:
            temp.husband = Person.people[person["husband"]]
            temp.husband.wife = temp
    return person_list
