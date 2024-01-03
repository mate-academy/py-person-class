class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people.update({name: self})


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]
    for index, person in enumerate(people):
        if "wife" in person and person["wife"]:
            person_list[index].wife = Person.people[person["wife"]]
        elif "husband" in person and person["husband"]:
            person_list[index].husband = Person.people[person["husband"]]
    return person_list
