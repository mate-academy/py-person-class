class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(peoples: list) -> list:
    people_list = []
    for person in peoples:
        Person(person["name"], person["age"])

    for person in peoples:
        people_list.append(Person.people[person["name"]])
        if "wife" in person.keys() and person["wife"]:
            people_list[-1].wife = Person.people[person["wife"]]

        if "husband" in person.keys() and person["husband"]:
            people_list[-1].husband = Person.people[person["husband"]]

    return people_list
