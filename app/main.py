class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    for person in people:
        if person["name"] not in Person.people:
            Person(person["name"], person["age"])
    for person in people:
        prsn = Person.people[person["name"]]
        if "husband" in person and person["husband"] is not None:
            prsn.husband = Person.people.get(person["husband"])
            if prsn.husband is not None:
                prsn.husband.wife = prsn
        if "wife" in person and person["wife"] is not None:
            prsn.wife = Person.people.get(person["wife"])
            if prsn.wife is not None:
                prsn.wife.husband = prsn
    return list(Person.people.values())
