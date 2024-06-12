class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(peoples: list) -> list:
    people_list = [Person(person["name"], person["age"]) for person in peoples]

    for person in peoples:
        if person.get("wife", ""):
            Person.people[person["name"]].wife = Person.people[person["wife"]]

        if person.get("husband", ""):
            Person.people[person["name"]].husband \
                = Person.people[person["husband"]]

    return people_list
