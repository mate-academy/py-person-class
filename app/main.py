class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife_or_husband = None
        self.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for one_person in people:
        name = one_person["name"]
        age = one_person["age"]
        person = Person(name, age)
        person_list.append(person)
    for spouse in people:
        if spouse.get("wife") is not None:
            Person.people[spouse["name"]].wife = Person.people[spouse["wife"]]
        if spouse.get("husband") is not None:
            Person.people[spouse["name"]].husband = Person.people[
                spouse["husband"]
            ]
    return person_list
