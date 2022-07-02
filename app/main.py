class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

        Person.people.update({
            name: self
        })


def create_person_list(people: list) -> list:
    person_list = [Person(i["name"], i["age"]) for i in people]

    for i in range(len(people)):

        if list(people[i].values())[2] is not None:
            if list(people[i].keys())[2] == "wife":
                person_list[i].wife = Person.people[people[i]["wife"]]
            else:
                person_list[i].husband = Person.people[people[i]["husband"]]

    return person_list
