class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people_list: list[dict]) -> list[Person]:
    new_person_list = [
        Person(person["name"], person["age"])
        for person in people_list
    ]

    for person in people_list:
        if person.get("wife"):
            Person.people[person["wife"]].husband\
                = Person.people[person["name"]]
        if person.get("husband"):
            Person.people[person["husband"]].wife\
                = Person.people[person["name"]]

    return new_person_list
