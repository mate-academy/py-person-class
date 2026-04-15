class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for i_person in people:
        person_list.append(Person(i_person["name"], i_person["age"]))
    persons = Person.people
    for i_person in people:
        if "wife" in i_person and i_person["wife"] is not None:
            persons[i_person["name"]].wife = persons[i_person["wife"]]
        elif "husband" in i_person and i_person["husband"] is not None:
            persons[i_person["name"]].husband = persons[i_person["husband"]]
    return person_list
