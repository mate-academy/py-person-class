class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_list: list) -> list:
    person_instances = [Person(person["name"], person["age"])
                        for person in people_list]

    for person in people_list:
        if person.get("wife"):
            Person.people[person["name"]].wife = Person.people[person["wife"]]
        if person.get("husband"):
            Person.people[person["name"]].husband \
                = Person.people[person["husband"]]

    return person_instances
