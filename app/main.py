class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(peoples: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in peoples]
    for person in peoples:
        if "wife" in person and person["wife"]:
            wife = Person.people[person["wife"]]
            Person.people[person["name"]].wife = wife
        elif "husband" in person and person["husband"]:
            husband = Person.people[person["husband"]]
            Person.people[person["name"]].husband = husband

    return person_list
