class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for new_person in people:
        person_list.append(Person(new_person["name"], new_person["age"]))
    for i in range(len(people)):
        if "wife" in people[i] and people[i]["wife"]:
            person_list[i].wife = Person.people[people[i]["wife"]]
        elif "husband" in people[i] and people[i]["husband"]:
            person_list[i].husband = Person.people[people[i]["husband"]]
    return person_list
