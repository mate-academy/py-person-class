class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list[Person]:
    people_list = [Person(person["name"], person["age"]) for person in people]
    for checked_person in people:
        if checked_person.get("wife"):
            Person.people[checked_person["name"]].wife = (
                Person.people[checked_person["wife"]]
            )
        if checked_person.get("husband"):
            Person.people[checked_person["name"]].husband = (
                Person.people[checked_person["husband"]]
            )
    return people_list
