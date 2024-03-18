class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    people_by_name = []

    for person in people:
        person_by_name = Person(person["name"], person["age"])
        people_by_name.append(person_by_name)

    for person in people:
        if person.get("wife"):
            Person.people[person["name"]].wife = (
                Person.people)[person["wife"]]
        if person.get("husband"):
            Person.people[person["name"]].husband = (
                Person.people)[person["husband"]]

    return people_by_name
