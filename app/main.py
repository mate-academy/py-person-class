class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife_or_husband = None
        self.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [
        Person(name=one_person["name"], age=one_person["age"])
        for one_person in people
    ]
    for person in people:
        if person.get("wife") is not None:
            Person.people[person["name"]].wife = Person.people[person["wife"]]
        if person.get("husband") is not None:
            Person.people[person["name"]].husband = Person.people[
                person["husband"]
            ]
    return person_list
