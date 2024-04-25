class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people_data: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people_data]

    for person in people_data:
        person_instance = Person.people[person["name"]]
        if person.get("wife"):
            person_instance.wife = Person.people[person["wife"]]
        elif person.get("husband"):
            person_instance.husband = Person.people[person["husband"]]

    return person_list
