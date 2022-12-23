class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people.update({name: self})


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        person_list.append(Person(person["name"], person["age"]))

    for index, person in enumerate(people):
        if "husband" in person.keys() and person["husband"]:
            person_list[index].husband = Person.people[person["husband"]]
        elif "wife" in person.keys() and person["wife"]:
            person_list[index].wife = Person.people[person["wife"]]
    return person_list
