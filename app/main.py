class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people.update({self.name: self})


def create_person_list(people: list) -> list:
    people_list = []
    for person in people:
        people_list.append(Person(person["name"], person["age"]))

    person_list = Person.people
    for person in people:
        if "wife" in person and person["wife"]:
            person_list[person["name"]].wife = person_list[person["wife"]]
        if "husband" in person and person["husband"]:
            person_list[person["name"]].husband =\
                person_list[person["husband"]]

    return people_list
