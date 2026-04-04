class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
    pass


def create_person_list(people: list) -> list:
    people_list = []
    for person in people:
        Person.people[person["name"]] = Person(person["name"], person["age"])
        people_list.append(Person.people[person["name"]])
    for person in people:
        if "wife" in person and person["wife"] is not None:
            person_name = person["wife"]
            Person.people[person["name"]].wife = Person.people[person_name]
        if "husband" in person and person["husband"] is not None:
            person_name = person["husband"]
            Person.people[person["name"]].husband = Person.people[person_name]

    return people_list
