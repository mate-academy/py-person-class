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

    for i in range(len(people_list)):
        if people[i].get("wife"):
            people_list[i].wife = Person.people.get(people[i]["wife"])
            continue
        if people[i].get("husband"):
            people_list[i].husband = Person.people.get(people[i]["husband"])

    return people_list
