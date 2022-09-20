class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people.update({self.name: self})


def create_person_list(people: list) -> list:
    people_arr = []
    for person in people:
        people_arr.append(Person(person["name"], person["age"]))
    for i in range(len(people)):
        if people[i].get("wife"):
            people_arr[i].wife = Person.people[people[i]["wife"]]
        if people[i].get("husband"):
            people_arr[i].husband = Person.people[people[i]["husband"]]
    return people_arr
