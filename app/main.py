class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    people_lst = []
    for i in people:
        people_lst.append(Person(i["name"], i["age"]))
    for i in people:
        person = Person.people[i["name"]]
        if "wife" in i and i["wife"] is not None:
            person.wife = Person.people[i["wife"]]
        if "husband" in i and i["husband"] is not None:
            person.husband = Person.people[i["husband"]]
    return people_lst
