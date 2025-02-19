class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_info: list) -> list:
    people_list = []

    for info in people_info:
        person = Person(info["name"], info["age"])
        people_list.append(person)

    for info in people_info:
        person = Person.people[info["name"]]

        if "wife" in info and info["wife"] is not None:
            person.wife = Person.people[info["wife"]]
            person.wife.husband = Person.people[info["name"]]

        if "husband" in info and info["husband"] is not None:
            person.husband = Person.people[info["husband"]]
            person.husband.wife = Person.people[info["name"]]
    return people_list
