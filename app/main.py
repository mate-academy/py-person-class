class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    people_list = []
    for person in people:
        people_list.append(Person(person["name"], person["age"]))
    for person_married in people:
        if "wife" in person_married and person_married["wife"]:
            Person.people[person_married["name"]].wife =\
                Person.people[person_married["wife"]]
        elif "husband" in person_married and person_married["husband"]:
            Person.people[person_married["name"]].husband =\
                Person.people[person_married["husband"]]
    return people_list
