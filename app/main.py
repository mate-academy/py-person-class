class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[name] = self


def create_person_list(people: list) -> list:
    person_instances = [
        Person(person_data["name"], person_data["age"])
        for person_data in people
    ]

    for person in people:
        person_name = person["name"]
        if person.get("wife"):
            spouse_name = person["wife"]
            Person.people[person_name].wife = Person.people[spouse_name]
        if person.get("husband"):
            spouse_name = person["husband"]
            Person.people[person_name].husband = Person.people[spouse_name]

    return person_instances
