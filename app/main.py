class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    list_of_object = []
    for dictionary in people:
        person_new = Person(name=dictionary["name"], age=dictionary["age"])
        list_of_object.append(person_new)
    for i in range(len(people)):
        if "wife" in people[i].keys():
            if people[i]["wife"] in Person.people:
                list_of_object[i].wife = Person.people[people[i]["wife"]]
        if "husband" in people[i].keys():
            if people[i]["husband"] in Person.people:
                list_of_object[i].husband = Person.people[people[i]["husband"]]
    return list_of_object
