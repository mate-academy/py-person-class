class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people.update({name: self})


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        person_instance = Person(person["name"], person["age"])
        person_list.append(person_instance)

    for index, person in enumerate(people):
        if person.get("wife", None):
            person_list[index].wife = Person.people[person["wife"]]
        elif person.get("husband", None):
            person_list[index].husband = Person.people[person["husband"]]

    return person_list
