class Person:

    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.people[self.name] = self

    def __repr__(self):
        print(f"name is {self.name} age is {self.age}")


def create_person_list(people: list) -> list:

    people_list = []

    for each in people:
        person = Person(each["name"], each["age"])
        people_list.append(person)

    for i in range(len(people)):
        if "wife" in people[i] and None is not people[i]["wife"]:
            people_list[i].wife = Person.people[people[i]["wife"]]
        if "husband" in people[i] and None is not people[i]["husband"]:
            people_list[i].husband = Person.people[people[i]["husband"]]

    return people_list
