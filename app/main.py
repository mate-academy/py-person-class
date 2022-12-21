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

    for i in range(len(people)):
        if "husband" in people[i].keys() and people[i]["husband"]:
            person_list[i].husband = Person.people[people[i]["husband"]]
        elif "wife" in people[i].keys() and people[i]["wife"]:
            person_list[i].wife = Person.people[people[i]["wife"]]

    return person_list
