class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    people_list = [Person(person["name"], person["age"]) for person in people]
    for person in people:
        get_person = Person.people[person["name"]]
        if person.get("wife"):
            get_person.wife = Person.people[person["wife"]]
        elif person.get("husband"):
            get_person.husband = Person.people[person["husband"]]
    return people_list


