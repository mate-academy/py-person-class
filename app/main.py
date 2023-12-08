class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_list: list) -> list:
    for person in people_list:
        Person(person["name"], person["age"])

    for person in people_list:
        if "wife" in person and person["wife"] is not None:
            Person.people[person["name"]].wife = Person.people[person["wife"]]
        elif "husband" in person and person["husband"] is not None:
            person_name = Person.people[person["name"]]
            person_husband = Person.people[person["husband"]]
            person_name.husband = person_husband

    return list(Person.people.values())
