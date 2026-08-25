class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    people_list = []
    for person in people:
        new_person = Person(person["name"], person["age"])
        people_list.append(new_person)
    for person in people:
        if "wife" in person.keys() and person["wife"]:
            Person.people[person["name"]].wife = Person.people[person["wife"]]
        if "husband" in person.keys() and person["husband"]:
            Person.people[person["name"]].husband = (
                Person.people)[person["husband"]]
    return people_list
